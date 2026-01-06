<template>
  <div class="edit-task-view">
    <div v-if="loading" class="loading">
      <p>Загрузка задачи...</p>
    </div>
    <div v-else-if="task">
      <TaskForm :initialTask="task" />
    </div>
    <div v-else class="not-found">
      <LayoutCard>
        <div style="text-align: center; padding: 40px;">
          <h2>😕 Задача не найдена</h2>
          <p>К сожалению, запрашиваемая задача не существует</p>
          <router-link to="/tasks" class="btn btn-primary">
            ← Вернуться к задачам
          </router-link>
        </div>
      </LayoutCard>
    </div>
  </div>
</template>

<script>
import TaskForm from '../components/TaskForm.vue'
import LayoutCard from '../components/LayoutCard.vue'
import api from '../services/api'

export default {
  name: 'EditTaskView',
  components: {
    TaskForm,
    LayoutCard
  },
  data() {
    return {
      task: null,
      loading: true
    }
  },
  async mounted() {
    try {
      const taskId = this.$route.params.id
      const tasks = await api.getTasks()
      this.task = tasks.find(t => t.id === parseInt(taskId))
    } catch (error) {
      console.error('Error loading task:', error)
    } finally {
      this.loading = false
    }
  }
}
</script>

<style scoped>
.edit-task-view {
  display: flex;
  justify-content: center;
}

.loading {
  text-align: center;
  padding: 60px 20px;
  color: white;
  font-size: 18px;
}

.not-found {
  display: flex;
  justify-content: center;
}
</style>
