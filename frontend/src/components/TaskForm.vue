<template>
  <LayoutCard title="Создание/Редактирование задачи">
    <form @submit.prevent="submitForm" class="task-form">
      <div class="form-group">
        <label for="title">Заголовок *</label>
        <input
          id="title"
          v-model.trim="form.title"
          type="text"
          placeholder="Введите название задачи"
          required
          @blur="validateTitle"
        />
        <span v-if="errors.title" class="error-message">{{ errors.title }}</span>
      </div>

      <div class="form-group">
        <label for="description">Описание</label>
        <textarea
          id="description"
          v-model.trim="form.description"
          placeholder="Введите подробное описание задачи"
        />
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="priority">Приоритет *</label>
          <select v-model="form.priority" id="priority" required>
            <option value="low">Низкий</option>
            <option value="medium">Средний</option>
            <option value="high">Высокий</option>
          </select>
        </div>

        <div class="form-group">
          <label for="category">Категория *</label>
          <div class="radio-group">
            <label class="radio-label">
              <input
                type="radio"
                value="Работа"
                v-model="form.category"
                required
              />
              Работа
            </label>
            <label class="radio-label">
              <input
                type="radio"
                value="Личное"
                v-model="form.category"
                required
              />
              Личное
            </label>
            <label class="radio-label">
              <input
                type="radio"
                value="Учеба"
                v-model="form.category"
                required
              />
              Учеба
            </label>
            <label class="radio-label">
              <input
                type="radio"
                value="Другое"
                v-model="form.category"
                required
              />
              Другое
            </label>
          </div>
        </div>
      </div>

      <div class="form-group">
        <label class="checkbox-label">
          <input v-model="form.important" type="checkbox" />
          <span>Отметить как важное</span>
        </label>
      </div>

      <div class="form-actions">
        <button type="submit" class="btn btn-primary">
          {{ isEditMode ? '✏️ Обновить' : '➕ Создать' }}
        </button>
        <button type="button" @click="$router.back()" class="btn btn-secondary">
          ← Отмена
        </button>
      </div>

      <div v-if="successMessage" class="success-message">
        ✓ {{ successMessage }}
      </div>
      <div v-if="formError" class="form-error">
        ✗ {{ formError }}
      </div>
    </form>
  </LayoutCard>
</template>

<script>
import LayoutCard from './LayoutCard.vue'
import api from '../services/api'

export default {
  name: 'TaskForm',
  components: {
    LayoutCard
  },
  props: {
    initialTask: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      form: {
        title: '',
        description: '',
        priority: 'medium',
        category: 'Работа',
        important: false
      },
      errors: {
        title: ''
      },
      successMessage: '',
      formError: '',
      isEditMode: false
    }
  },
  watch: {
    initialTask: {
      immediate: true,
      handler(newVal) {
        if (newVal) {
          this.isEditMode = true
          this.form = { ...newVal }
        } else {
          this.isEditMode = false
          this.resetForm()
        }
      }
    }
  },
  methods: {
    validateTitle() {
      if (!this.form.title) {
        this.errors.title = 'Заголовок обязателен'
      } else if (this.form.title.length < 3) {
        this.errors.title = 'Заголовок должен содержать минимум 3 символа'
      } else if (this.form.title.length > 200) {
        this.errors.title = 'Заголовок не должен превышать 200 символов'
      } else {
        this.errors.title = ''
      }
    },
    async submitForm() {
      this.validateTitle()
      if (this.errors.title) return

      this.formError = ''
      this.successMessage = ''

      try {
        if (this.isEditMode) {
          await api.updateTask(this.form.id, this.form)
          this.successMessage = 'Задача успешно обновлена!'
          setTimeout(() => {
            this.$router.push('/tasks')
          }, 1500)
        } else {
          await api.createTask(this.form)
          this.successMessage = 'Задача успешно создана!'
          setTimeout(() => {
            this.$router.push('/tasks')
          }, 1500)
        }
      } catch (error) {
        this.formError = error.message || 'Ошибка при сохранении задачи'
      }
    },
    resetForm() {
      this.form = {
        title: '',
        description: '',
        priority: 'medium',
        category: 'Работа',
        important: false
      }
      this.errors.title = ''
      this.successMessage = ''
      this.formError = ''
    }
  }
}
</script>

<style scoped>
.task-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 600;
  color: #003d7a;
  font-size: 14px;
}

.form-group input,
.form-group textarea,
.form-group select {
  padding: 12px;
  border: 2px solid #e2e8f0;
  border-radius: 6px;
  font-size: 14px;
  font-family: inherit;
  transition: all 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: #0055b8;
  box-shadow: 0 0 0 3px rgba(0, 85, 184, 0.1);
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.radio-group {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.radio-label,
.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-weight: 500;
  color: #1f2937;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s ease;
}

.radio-label:hover,
.checkbox-label:hover {
  background: #f0f9ff;
}

.radio-label input[type="radio"],
.checkbox-label input[type="checkbox"] {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #0055b8;
}

.form-actions {
  display: flex;
  gap: 12px;
  margin-top: 12px;
}

.btn {
  flex: 1;
  padding: 12px 20px;
  font-size: 14px;
  font-weight: 600;
}

.error-message {
  color: #ef4444;
  font-size: 12px;
  margin-top: -4px;
}

.success-message {
  background: #d1fae5;
  color: #065f46;
  padding: 12px 16px;
  border-radius: 6px;
  border-left: 4px solid #10b981;
  font-weight: 500;
}

.form-error {
  background: #fee2e2;
  color: #7f1d1d;
  padding: 12px 16px;
  border-radius: 6px;
  border-left: 4px solid #ef4444;
  font-weight: 500;
}

@media (max-width: 768px) {
  .form-row,
  .radio-group {
    grid-template-columns: 1fr;
  }

  .form-actions {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>
