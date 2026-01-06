<template>
  <div class="tasks-view">
    <LayoutCard title="Управление задачами">
      <template #footer>
        <router-link to="/tasks/new" class="btn btn-primary">
          ➕ Новая задача
        </router-link>
      </template>
    </LayoutCard>

    <div class="content-wrapper">
      <TaskFilters
        :filters="filters"
        @update-filters="updateFilters"
      />

      <TaskList
        :tasks="tasks"
        :filters="filters"
        @toggle="toggleTask"
        @edit="editTask"
        @delete="deleteTask"
      />
    </div>

    <div v-if="loading" class="loading-spinner">
      <div class="spinner"></div>
      <p>Загрузка задач...</p>
    </div>

    <div v-if="error" class="error-alert">
      ✗ {{ error }}
      <button @click="loadTasks" class="btn btn-secondary btn-small">
        🔄 Повторить
      </button>
    </div>
  </div>
</template>

<script>
import LayoutCard from '../components/LayoutCard.vue'
import TaskList from '../components/TaskList.vue'
import TaskFilters from '../components/TaskFilters.vue'
import api from '../services/api'

export default {
  name: 'TasksView',
  components: {
    LayoutCard,
    TaskList,
    TaskFilters
  },
  data() {
    return {
      tasks: [],
      loading: false,
      error: null,
      filters: {
        status: 'all',
        sort: 'date-desc',
        search: ''
      }
    }
  },
  async mounted() {
    await this.loadTasks()
  },
  methods: {
    async loadTasks() {
      this.loading = true
      this.error = null
      try {
        this.tasks = await api.getTasks()
      } catch (error) {
        this.error = 'Не удалось загрузить задачи. Попробуйте позже.'
        console.error('Error loading tasks:', error)
      } finally {
        this.loading = false
      }
    },
    updateFilters(newFilters) {
      this.filters = newFilters
    },
    async toggleTask(taskId) {
      try {
        const task = this.tasks.find(t => t.id === taskId)
        if (task) {
          await api.updateTask(taskId, { ...task, completed: !task.completed })
          await this.loadTasks()
        }
      } catch (error) {
        this.error = 'Не удалось обновить статус задачи'
      }
    },
    editTask(taskId) {
      this.$router.push(`/tasks/${taskId}/edit`)
    },
    async deleteTask(taskId) {
      if (confirm('Вы уверены, что хотите удалить эту задачу?')) {
        try {
          await api.deleteTask(taskId)
          await this.loadTasks()
        } catch (error) {
          this.error = 'Не удалось удалить задачу'
        }
      }
    }
  }
}
</script>

<style scoped>
.tasks-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.content-wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.loading-spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #6b7280;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e2e8f0;
  border-top-color: #0055b8;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-alert {
  background: #fee2e2;
  color: #7f1d1d;
  padding: 16px;
  border-radius: 8px;
  border-left: 4px solid #ef4444;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

@media (max-width: 768px) {
  .error-alert {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
