<template>
  <div class="create-task-view">
    <TaskForm />
  </div>
</template>

<script>
import TaskForm from '../components/TaskForm.vue'

export default {
  name: 'CreateTaskView',
  components: {
    TaskForm
  }
}
</script>

<style scoped>
.create-task-view {
  display: flex;
  justify-content: center;
}
</style>
