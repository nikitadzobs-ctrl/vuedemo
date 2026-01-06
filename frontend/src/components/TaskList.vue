<template>
  <div class="task-list-container">
    <div v-if="filteredTasks.length === 0" class="list-empty">
      <p>😴 Нет задач для отображения</p>
      <p style="font-size: 13px; margin-top: 8px; color: #9ca3af;">
        Попробуйте изменить фильтры или добавить новую задачу
      </p>
    </div>

    <div v-else class="tasks-list">
      <TaskItem
        v-for="task in filteredTasks"
        :key="task.id"
        :task="task"
        @toggle="$emit('toggle', $event)"
        @edit="$emit('edit', $event)"
        @delete="$emit('delete', $event)"
      />
    </div>
  </div>
</template>

<script>
import TaskItem from './TaskItem.vue'

export default {
  name: 'TaskList',
  components: {
    TaskItem
  },
  props: {
    tasks: {
      type: Array,
      default: () => []
    },
    filters: {
      type: Object,
      default: () => ({
        status: 'all',
        sort: 'date-desc',
        search: ''
      })
    }
  },
  emits: ['toggle', 'edit', 'delete'],
  computed: {
    filteredTasks() {
      let result = [...this.tasks]

      // Фильтрация по статусу
      if (this.filters.status === 'completed') {
        result = result.filter(t => t.completed)
      } else if (this.filters.status === 'pending') {
        result = result.filter(t => !t.completed)
      }

      // Фильтрация по поиску
      if (this.filters.search) {
        const search = this.filters.search.toLowerCase()
        result = result.filter(t =>
          t.title.toLowerCase().includes(search) ||
          (t.description && t.description.toLowerCase().includes(search))
        )
      }

      // Сортировка
      switch (this.filters.sort) {
        case 'date-asc':
          result.sort((a, b) => new Date(a.created_at) - new Date(b.created_at))
          break
        case 'title-asc':
          result.sort((a, b) => a.title.localeCompare(b.title, 'ru'))
          break
        case 'title-desc':
          result.sort((a, b) => b.title.localeCompare(a.title, 'ru'))
          break
        case 'priority':
          const priorityOrder = { high: 0, medium: 1, low: 2 }
          result.sort((a, b) => (priorityOrder[a.priority] || 3) - (priorityOrder[b.priority] || 3))
          break
        case 'date-desc':
        default:
          result.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
          break
      }

      return result
    }
  }
}
</script>

<style scoped>
.task-list-container {
  width: 100%;
}

.tasks-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.list-empty {
  text-align: center;
  padding: 60px 20px;
  background: white;
  border-radius: 12px;
  color: #6b7280;
  font-size: 16px;
}

@media (max-width: 768px) {
  .list-empty {
    padding: 40px 20px;
    font-size: 14px;
  }
}
</style>
