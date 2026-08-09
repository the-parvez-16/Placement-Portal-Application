<script setup>
defineProps({
  drives: {
    type: Array,
    default: () => []
  }
});
</script>

<template>
  <section class="portal-card p-3 mb-4">
    <h2 class="fs-6 fw-bold border-bottom border-dark pb-2 mb-3">Closed Drives</h2>

    <div class="table-responsive">
        <table class="table table-sm mb-0" style="font-size:14px;">
            <thead>
                <tr>
                    <th>Sr.</th>
                    <th>Drive Name</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="drive in drives" :key="drive.id">
                    <td>{{ drive.id }}</td>
                    <td>{{ drive.job_title }}</td>
                    <td>
                        <div class="d-flex gap-2 flex-wrap">
                            <router-link :to="`/company/drive/${drive.id}`" class="portal-btn portal-btn-dark text-decoration-none">View Details</router-link>
                            <button class="portal-btn portal-btn-primary">Re-open Drive</button>
                        </div>
                    </td>
                </tr>
                <tr v-if="drives.length === 0">
                    <td colspan="3" class="text-center text-muted py-3">No closed drives yet.</td>
                </tr>
            </tbody>
        </table>
    </div>
  </section>
</template>