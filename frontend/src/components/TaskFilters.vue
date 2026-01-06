<template>
  <LayoutCard title="Управление фильтрацией и сортировкой">
    <div class="filters-container">
      <div class="filter-group">
        <label>Статус</label>
        <select v-model="localFilters.status" @change="updateFilters" class="filter-select">
          <option value="all">Все задачи</option>
          <option value="completed">Выполненные</option>
          <option value="pending">Невыполненные</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Сортировка</label>
        <select v-model="localFilters.sort" @change="updateFilters" class="filter-select">
          <option value="date-desc">По дате (новые сначала)</option>
          <option value="date-asc">По дате (старые сначала)</option>
          <option value="title-asc">По названию (А-Я)</option>
          <option value="title-desc">По названию (Я-А)</option>
          <option value="priority">По приоритету</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Поиск</label>
        <input
          v-model="localFilters.search"
          @input="updateFilters"
          type="text"
          placeholder="Поиск задач..."
          class="filter-input"
        />
      </div>

      <div class="filter-actions">
        <button @click="resetFilters" class="btn btn-secondary btn-small">
          🔄 Сбросить
        </button>
      </div>
    </div>
  </LayoutCard>
</template>

<script>
export default {
  name: 'TaskFilters',
  props: {
    filters: {
      type: Object,
      default: () => ({
        status: 'all',
        sort: 'date-desc',
        search: ''
      })
    }
  },
  data() {
    return {
      localFilters: { ...this.filters }
    }
  },
  watch: {
    filters: {
      handler(newVal) {
        this.localFilters = { ...newVal }
      },
      deep: true
    }
  },
  methods: {
    updateFilters() {
      this.$emit('update-filters', { ...this.localFilters })
    },
    resetFilters() {
      this.localFilters = {
        status: 'all',
        sort: 'date-desc',
        search: ''
      }
      this.updateFilters()
    }
  }
}
</script>

<style scoped>
.filters-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  align-items: flex-end;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.filter-group label {
  font-weight: 600;
  color: #003d7a;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.filter-select,
.filter-input {
  padding: 10px 12px;
  border: 2px solid #e2e8f0;
  border-radius: 6px;
  font-size: 14px;
  transition: all 0.3s ease;
  font-family: inherit;
}

.filter-select:focus,
.filter-input:focus {
  outline: none;
  border-color: #0055b8;
  box-shadow: 0 0 0 3px rgba(0, 85, 184, 0.1);
}

.filter-actions {
  display: flex;
  gap: 8px;
}

@media (max-width: 768px) {
  .filters-container {
    grid-template-columns: 1fr;
  }

  .filter-actions {
    width: 100%;
  }

  .btn {
    width: 100%;
  }
}
</style>
