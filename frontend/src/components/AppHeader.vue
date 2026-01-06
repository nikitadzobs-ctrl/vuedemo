<template>
  <header class="app-header">
    <div class="header-container">
      <div class="logo-section">
        <h1 class="logo">📋 Менеджер задач</h1>
      </div>
      <nav class="nav-menu">
        <router-link to="/" class="nav-link" :class="{ active: isActive('/') }">
          Главная
        </router-link>
        <router-link to="/tasks" class="nav-link" :class="{ active: isActive('/tasks') }">
          Задачи
        </router-link>
      </nav>
    </div>
  </header>
</template>

<script>
import { useRoute } from 'vue-router'

export default {
  name: 'AppHeader',
  setup() {
    const route = useRoute()

    const isActive = (path) => {
      return route.path.startsWith(path) && (path === '/' ? route.path === '/' : true)
    }

    return { isActive }
  }
}
</script>

<style scoped>
.app-header {
  background: linear-gradient(135deg, #003d7a 0%, #0055b8 100%);
  color: white;
  padding: 16px 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  border-bottom: 3px solid #60a5fa;
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo-section {
  flex: 1;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  margin: 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.nav-menu {
  display: flex;
  gap: 20px;
  align-items: center;
}

.nav-link {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 6px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-link.active {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.3);
}

@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
    gap: 16px;
  }

  .logo {
    font-size: 20px;
  }

  .nav-menu {
    gap: 10px;
  }

  .nav-link {
    padding: 6px 12px;
    font-size: 14px;
  }
}
</style>
