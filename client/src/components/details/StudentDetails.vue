<script setup>
import { computed } from 'vue';
import { authState } from '@/store';

defineProps({ student: Object });
const isAdmin = computed(() => authState.value.role === 'admin' || authState.value.role === 'sudo');

const toggleStatus = (action, id) => {
    console.log(`${action}ing student ${id}`);
};
</script>

<template>
  <section class="portal-card p-4 mb-4 mt-2">
      <div class="border-bottom border-dark pb-3 mb-4 d-flex flex-wrap justify-content-between align-items-center gap-3">
          <div>
              <h2 class="fs-4 fw-bold mb-1">{{ student.name }}</h2>
              <span class="fs-6 fw-bold text-muted">{{ student.email }}</span>
          </div>
          <span class="portal-btn portal-btn-dark" style="pointer-events: none;">Status: {{ student.status }}</span>
      </div>

      <div class="mb-4">
          <strong class="d-block mb-2 border-bottom border-dark pb-1 fs-5">Education History</strong>
          <p style="white-space: pre-wrap; font-size: 15px; line-height: 1.6;">{{ student.education || 'Not Provided' }}</p>
      </div>

      <div class="mb-4">
          <strong class="d-block mb-2 border-bottom border-dark pb-1 fs-5">Technical & Soft Skills</strong>
          <p style="white-space: pre-wrap; font-size: 15px; line-height: 1.6;">{{ student.skills || 'Not Provided' }}</p>
      </div>

      <div class="mb-4">
          <strong class="d-block mb-2 border-bottom border-dark pb-1 fs-5">Resume Document</strong>
          <a v-if="student.resume_file" :href="student.resume_file" target="_blank" class="text-decoration-none portal-btn portal-btn-primary mb-0 d-inline-block mt-2">View Resume ↗</a>
          <p v-else class="text-muted fst-italic mt-2 mb-0">No resume link provided.</p>
      </div>

      <div v-if="isAdmin" class="d-flex gap-2 border-top border-dark pt-3 mt-4 justify-content-end">
          <button v-if="student.status === 'APPROVED'" @click="toggleStatus('blacklist', student.id)" class="portal-btn portal-btn-danger mb-0">Blacklist Student</button>
          <button v-else-if="student.status === 'BLOCKED'" @click="toggleStatus('unblock', student.id)" class="portal-btn portal-btn-success mb-0">Unblock Student</button>
      </div>
  </section>
</template>