<template>
  <div class="layout-card">
    <div v-if="title" class="card-header">
      {{ title }}
    </div>
    <div class="card-body">
      <slot />
    </div>
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'LayoutCard',
  props: {
    title: {
      type: String,
      default: null
    }
  }
}
</script>

<style scoped>
.layout-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: all 0.3s ease;
}

.layout-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.card-header {
  background: linear-gradient(135deg, #003d7a 0%, #0055b8 100%);
  color: white;
  padding: 16px 20px;
  font-weight: 600;
  font-size: 16px;
  border-bottom: 3px solid #60a5fa;
}

.card-body {
  padding: 20px;
}

.card-footer {
  background: #f8fafc;
  padding: 16px 20px;
  border-top: 1px solid #e2e8f0;
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

@media (max-width: 768px) {
  .card-body {
    padding: 15px;
  }

  .card-footer {
    flex-direction: column;
  }
}
</style>
