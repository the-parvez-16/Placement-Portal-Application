<script setup>
defineProps({
  status: {
    type: String,
    required: true
  }
});
</script>

<template>
  <div>
    <!-- PENDING -->
    <div v-if="status === 'PENDING'" class="portal-card p-5 text-center mt-4">
        <h2 class="fs-4 fw-bold mb-3">Welcome! Let's get started.</h2>
        <p class="text-muted mb-4">Please complete your company profile so the admin can review your application.</p>
        <router-link to="/company/profile" class="portal-btn portal-btn-primary" style="font-size: 16px; padding: 8px 20px;">
            Complete Profile →
        </router-link>
    </div>

    <!-- APPLIED -->
    <div v-else-if="status === 'APPLIED'" class="portal-card p-5 text-center mt-4 border-warning">
        <h2 class="fs-4 fw-bold mb-3 text-warning">Application Under Review</h2>
        <p class="text-muted mb-0">Your profile has been submitted successfully. Please wait while the Admin approves your account.</p>
    </div>

    <!-- BLOCKED -->
    <div v-else-if="status === 'BLOCKED'" class="portal-card p-5 text-center mt-4 border-danger">
        <h2 class="fs-4 fw-bold mb-3 text-danger">Account Suspended</h2>
        <p class="text-muted mb-0">Your company account has been blacklisted. You cannot create new drives or view applications.</p>
        <p class="text-muted mt-2">Please contact the placement cell administration for more details.</p>
    </div>
  </div>
</template>