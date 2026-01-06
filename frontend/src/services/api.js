import axios from 'axios'

const API_BASE_URL = '/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000
})

export default {
  async getTasks() {
    try {
      const response = await api.get('/tasks')
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || error.message || 'Error fetching tasks')
    }
  },

  async getTask(id) {
    try {
      const response = await api.get(`/tasks/${id}`)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || error.message || 'Error fetching task')
    }
  },

  async createTask(taskData) {
    try {
      const response = await api.post('/tasks', taskData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || error.message || 'Error creating task')
    }
  },

  async updateTask(id, taskData) {
    try {
      const response = await api.put(`/tasks/${id}`, taskData)
      return response.data
    } catch (error) {
      throw new Error(error.response?.data?.detail || error.message || 'Error updating task')
    }
  },

  async deleteTask(id) {
    try {
      await api.delete(`/tasks/${id}`)
    } catch (error) {
      throw new Error(error.response?.data?.detail || error.message || 'Error deleting task')
    }
  }
}
