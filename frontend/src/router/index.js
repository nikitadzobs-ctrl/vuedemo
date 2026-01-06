import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TasksView from '../views/TasksView.vue'
import CreateTaskView from '../views/CreateTaskView.vue'
import EditTaskView from '../views/EditTaskView.vue'
import NotFoundView from '../views/NotFoundView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: TasksView
  },
  {
    path: '/tasks/new',
    name: 'CreateTask',
    component: CreateTaskView
  },
  {
    path: '/tasks/:id/edit',
    name: 'EditTask',
    component: EditTaskView
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFoundView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
