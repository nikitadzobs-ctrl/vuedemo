<template>
  <div class="not-found-view">
    <LayoutCard>
      <div class="not-found-content">
        <div class="not-found-icon">404</div>
        <h1 class="not-found-title">Страница не найдена</h1>
        <p class="not-found-description">
          К сожалению, запрашиваемая страница не существует или была удалена.
        </p>
        <div class="not-found-actions">
          <router-link to="/" class="btn btn-primary">
            🏠 На главную
          </router-link>
          <router-link to="/tasks" class="btn btn-secondary">
            📋 К задачам
          </router-link>
        </div>
      </div>
    </LayoutCard>
  </div>
</template>

<script>
import LayoutCard from '../components/LayoutCard.vue'

export default {
  name: 'NotFoundView',
  components: {
    LayoutCard
  }
}
</script>

<style scoped>
.not-found-view {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 240px);
}

.not-found-content {
  text-align: center;
  padding: 40px;
}

.not-found-icon {
  font-size: 120px;
  font-weight: 700;
  background: linear-gradient(135deg, #003d7a 0%, #0055b8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 20px;
}

.not-found-title {
  font-size: 36px;
  font-weight: 700;
  color: #003d7a;
  margin-bottom: 16px;
}

.not-found-description {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 32px;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}

.not-found-actions {
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
  .not-found-view {
    min-height: auto;
  }

  .not-found-icon {
    font-size: 80px;
  }

  .not-found-title {
    font-size: 28px;
  }

  .not-found-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
