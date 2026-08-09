<script setup>
import { alertState } from "@/store";

const closeToast = () => {
  alertState.value.message = "";
};
</script>

<template>
  <div class="toast-container position-fixed top-0 end-0 p-3" style="z-index: 1055;">
    <div 
      v-if="alertState.message" 
      class="toast show portal-toast align-items-center border-0" 
      :class="`toast-${alertState.type || 'info'}`" 
      role="alert"
    >
      <div class="d-flex w-100 p-2">
        <div class="toast-body fw-bold flex-grow-1 p-1">
          {{ alertState.message }}
        </div>
        <button type="button" class="btn-close m-auto me-2" @click="closeToast"></button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.portal-toast {
    min-width: 280px;
    border-radius: 5px;
    box-shadow: 4px 4px 0 rgba(50, 50, 50, 0.1);
    backdrop-filter: blur(5px);
}

.toast-success {
    border-left: 6px solid var(--success) !important;
    background-color: rgba(25, 135, 84, 0.15) !important;
    color: #146c43;
}

.toast-danger {
    border-left: 6px solid var(--danger, #dc3545) !important;
    background-color: rgba(220, 53, 69, 0.15) !important;
    color: #b02a37;
}

.toast-warning {
    border-left: 6px solid #ffc107 !important;
    background-color: rgba(255, 193, 7, 0.2) !important;
    color: #997404;
}

.toast-info {
    border-left: 6px solid var(--primary, #2d8cf0) !important;
    background-color: rgba(45, 140, 240, 0.15) !important;
    color: #1a5696;
}

</style>