<script setup>
defineProps({
  drives: {
    type: Array,
    default: () => []
  }
});
const emit = defineEmits(['updateStatus']);
</script>

<template>
  <section class="portal-card p-3 mb-4">
    <div class="d-flex justify-content-between align-items-center border-bottom border-dark pb-2 mb-3">
        <h2 class="fs-6 fw-bold mb-0">Upcoming Drives</h2>
        <button class="portal-btn portal-btn-primary d-flex align-items-center" data-bs-toggle="modal" data-bs-target="#createDriveModal">
            <VsxIcon iconName="AddSquare" :size="20" type="linear" />&nbsp;Create Drive
        </button>
    </div>

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
                            <router-link :to="`/drive/${drive.id}`" class="portal-btn portal-btn-dark">View Details</router-link>
                            <button @click="$emit('updateStatus', drive.id, 'closed')" class="portal-btn portal-btn-success">Mark as Complose</button>
                        </div>
                    </td>
                </tr>
                <tr v-if="drives.length === 0">
                    <td colspan="3" class="text-center text-muted py-3">No upcoming drives.</td>
                </tr>
            </tbody>
        </table>
    </div>
  </section>
</template>