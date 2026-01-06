<template>
  <footer class="app-footer">
    <div class="footer-container">
      <div class="footer-content">
        <p>&copy; 2024 Менеджер задач. Все права защищены.</p>
        <p class="footer-tech">
          Создано с Vue 3 & FastAPI 🚀
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
.app-footer {
  background: linear-gradient(135deg, #001a40 0%, #003d7a 100%);
  color: rgba(255, 255, 255, 0.8);
  padding: 24px 0;
  border-top: 2px solid #3b82f6;
  margin-top: auto;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-content {
  text-align: center;
}

.footer-content p {
  margin: 4px 0;
  font-size: 14px;
}

.footer-tech {
  color: #93c5fd;
  margin-top: 8px;
}

@media (max-width: 768px) {
  .app-footer {
    padding: 16px 0;
  }

  .footer-content p {
    font-size: 12px;
  }
}
</style>
