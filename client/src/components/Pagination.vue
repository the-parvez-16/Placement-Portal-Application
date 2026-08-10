<script setup>
defineProps({
  currentPage: { type: Number, required: true },
  totalPages: { type: Number, required: true }
});
defineEmits(['changePage']);
</script>

<template>
  <div class="d-flex justify-content-center gap-2 mt-4 pt-3 border-top border-dark">
    <button :disabled="currentPage === 1" @click="$emit('changePage', currentPage - 1)" class="portal-btn portal-btn-dark">
      ← Prev
    </button>
    <span class="fw-bold align-self-center px-3">Page {{ currentPage }} of {{ totalPages }}</span>
    <button :disabled="currentPage === totalPages" @click="$emit('changePage', currentPage + 1)" class="portal-btn portal-btn-dark">
      Next →
    </button>
  </div>
</template>