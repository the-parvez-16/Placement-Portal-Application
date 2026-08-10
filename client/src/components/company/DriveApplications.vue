<script setup>
defineProps({
  drives: {
    type: Array,
    default: () => []
  }
});
</script>

<template>
  <div>
    <section v-for="drive in drives" :key="'app-'+drive.id" class="portal-card p-3 mb-4">
        <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">
            Applications — {{ drive.job_title }}
        </h2>

        <template v-if="drive.applications && drive.applications.length > 0">
            <div v-for="app in drive.applications" :key="app.id" class="portal-list-row d-flex justify-content-between align-items-center py-2">
                <span>{{ app.student.name }}</span>
                <router-link :to="`/review/${app.id}`" class="portal-btn portal-btn-dark">Review Application</router-link>
            </div>
        </template>
        <p v-else class="text-muted mb-0">No applications received yet.</p>
    </section>
    
    <div v-if="drives.length === 0" class="portal-card p-3 text-center text-muted">
        Create a drive to start receiving applications.
    </div>
  </div>
</template>