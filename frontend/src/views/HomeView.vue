<template>
  <div class="home-view">
    <LayoutCard title="Добро пожаловать в Менеджер задач">
      <div class="welcome-content">
        <div class="welcome-icon">📋</div>
        <h2 class="welcome-title">Организуйте свои задачи эффективно</h2>
        <p class="welcome-description">
          Используйте наше приложение для управления задачами, отслеживания прогресса и повышения продуктивности.
        </p>

        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">✅</div>
            <h3>Простое управление</h3>
            <p>Легко создавайте, редактируйте и удаляйте задачи</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <h3>Фильтрация и сортировка</h3>
            <p>Находите нужные задачи с помощью мощных фильтров</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3>Приоритизация</h3>
            <p>Установите приоритеты для лучшей организации</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Статистика</h3>
            <p>Отслеживайте прогресс выполнения задач</p>
          </div>
        </div>

        <div class="welcome-stats" v-if="taskStats">
          <div class="stat-item">
            <span class="stat-number">{{ taskStats.total }}</span>
            <span class="stat-label">Всего задач</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">{{ taskStats.completed }}</span>
            <span class="stat-label">Выполнено</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">{{ taskStats.pending }}</span>
            <span class="stat-label">Осталось</span>
          </div>
        </div>

        <div class="welcome-actions">
          <router-link to="/tasks" class="btn btn-primary">
            → Перейти к задачам
          </router-link>
          <router-link to="/tasks/new" class="btn btn-secondary">
            ➕ Создать новую задачу
          </router-link>
        </div>
      </div>
    </LayoutCard>
  </div>
</template>

<script>
import LayoutCard from '../components/LayoutCard.vue'
import api from '../services/api'

export default {
  name: 'HomeView',
  components: {
    LayoutCard
  },
  data() {
    return {
      taskStats: null
    }
  },
  async mounted() {
    await this.loadStats()
  },
  methods: {
    async loadStats() {
      try {
        const tasks = await api.getTasks()
        this.taskStats = {
          total: tasks.length,
          completed: tasks.filter(t => t.completed).length,
          pending: tasks.filter(t => !t.completed).length
        }
      } catch (error) {
        console.error('Error loading stats:', error)
      }
    }
  }
}
</script>

<style scoped>
.home-view {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 240px);
}

.welcome-content {
  text-align: center;
}

.welcome-icon {
  font-size: 80px;
  margin-bottom: 20px;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.welcome-title {
  font-size: 32px;
  font-weight: 700;
  color: #003d7a;
  margin-bottom: 16px;
}

.welcome-description {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 32px;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 32px;
}

.feature-card {
  background: linear-gradient(135deg, #f0f9ff 0%, #eff6ff 100%);
  border: 2px solid #bfdbfe;
  border-radius: 10px;
  padding: 20px;
  transition: all 0.3s ease;
}

.feature-card:hover {
  border-color: #0055b8;
  box-shadow: 0 4px 12px rgba(0, 85, 184, 0.2);
  transform: translateY(-4px);
}

.feature-icon {
  font-size: 40px;
  margin-bottom: 12px;
}

.feature-card h3 {
  font-size: 16px;
  font-weight: 600;
  color: #003d7a;
  margin-bottom: 8px;
}

.feature-card p {
  font-size: 13px;
  color: #6b7280;
  line-height: 1.5;
}

.welcome-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 32px;
  padding: 24px;
  background: linear-gradient(135deg, #003d7a 0%, #0055b8 100%);
  border-radius: 10px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.stat-number {
  font-size: 32px;
  font-weight: 700;
  color: white;
}

.stat-label {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.8);
}

.welcome-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 12px 24px;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

@media (max-width: 768px) {
  .home-view {
    min-height: auto;
  }

  .welcome-title {
    font-size: 24px;
  }

  .welcome-description {
    font-size: 14px;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .welcome-stats {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .welcome-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
