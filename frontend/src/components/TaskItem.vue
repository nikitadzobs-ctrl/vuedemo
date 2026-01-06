<template>
  <div class="task-item" :class="{ completed: task.completed }">
    <div class="task-header">
      <div class="task-title-section">
        <input
          type="checkbox"
          :checked="task.completed"
          @change="$emit('toggle', task.id)"
          class="task-checkbox"
        />
        <h3 class="task-title">{{ task.title }}</h3>
        <span v-if="task.important" class="badge-important">⭐ Важно</span>
        <span class="priority-badge" :class="`priority-${task.priority}`">
          {{ priorityLabel }}
        </span>
      </div>
      <span class="category-badge">{{ task.category }}</span>
    </div>

    <p v-if="task.description" class="task-description">{{ task.description }}</p>

    <div class="task-footer">
      <span class="task-date">{{ formatDate(task.created_at) }}</span>
      <div class="task-actions">
        <button @click="$emit('edit', task.id)" class="btn btn-secondary btn-small">
          ✏️ Редактировать
        </button>
        <button @click="$emit('delete', task.id)" class="btn btn-danger btn-small">
          🗑️ Удалить
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TaskItem',
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  emits: ['toggle', 'edit', 'delete'],
  computed: {
    priorityLabel() {
      const labels = {
        low: 'Низкий',
        medium: 'Средний',
        high: 'Высокий'
      }
      return labels[this.task.priority] || this.task.priority
    }
  },
  methods: {
    formatDate(date) {
      if (!date) return ''
      const d = new Date(date)
      return d.toLocaleDateString('ru-RU', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  }
}
</script>

<style scoped>
.task-item {
  background: white;
  border: 2px solid #e2e8f0;
  border-left: 5px solid #0055b8;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 12px;
  transition: all 0.3s ease;
}

.task-item:hover {
  border-left-color: #60a5fa;
  box-shadow: 0 4px 12px rgba(0, 85, 184, 0.15);
  transform: translateX(4px);
}

.task-item.completed {
  background: #f0f9ff;
  border-left-color: #10b981;
}

.task-item.completed .task-title {
  text-decoration: line-through;
  color: #9ca3af;
}

.task-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 12px;
  flex-wrap: wrap;
  gap: 12px;
}

.task-title-section {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.task-checkbox {
  width: 20px;
  height: 20px;
  cursor: pointer;
  accent-color: #10b981;
  flex-shrink: 0;
}

.task-title {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
  color: #003d7a;
}

.badge-important {
  background: #fef3c7;
  color: #92400e;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.priority-badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}

.priority-low {
  background: #dbeafe;
  color: #003d7a;
}

.priority-medium {
  background: #fef08a;
  color: #713f12;
}

.priority-high {
  background: #fee2e2;
  color: #7f1d1d;
}

.category-badge {
  background: linear-gradient(135deg, #003d7a 0%, #0055b8 100%);
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
  align-self: center;
}

.task-description {
  color: #6b7280;
  font-size: 14px;
  margin: 12px 0;
  padding-left: 32px;
}

.task-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  border-top: 1px solid #e2e8f0;
  padding-top: 12px;
  margin-top: 12px;
}

.task-date {
  color: #9ca3af;
  font-size: 12px;
}

.task-actions {
  display: flex;
  gap: 8px;
}

@media (max-width: 768px) {
  .task-item {
    padding: 12px;
  }

  .task-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .task-title-section {
    width: 100%;
    flex-wrap: wrap;
  }

  .task-description {
    padding-left: 32px;
  }

  .task-footer {
    flex-direction: column;
    align-items: flex-start;
  }

  .task-actions {
    width: 100%;
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>
