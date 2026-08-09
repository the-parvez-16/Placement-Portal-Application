<script setup>
import { computed } from 'vue';
import { authState } from '@/store';
import CompanyDrives from './CompanyDrives.vue';

defineProps({ company: Object });
const isAdmin = computed(() => authState.value.role === 'admin' || authState.value.role === 'sudo');

const handleAction = (action, id) => {
    console.log(`${action} company ${id}`);
};
</script>

<template>
  <div>
    <section class="portal-card p-4 mb-4 mt-2">
        <div class="border-bottom border-dark pb-3 mb-4 d-flex flex-wrap justify-content-between align-items-center gap-3">
            <div>
                <h2 class="fs-4 fw-bold mb-1">{{ company.name }}</h2>
                <span class="fs-6 fw-bold text-muted">Status: {{ company.status }}</span>
            </div>
        </div>

        <div class="row mb-4 g-3">
            <div class="col-12 col-md-6">
                <strong class="d-block mb-1">Contact Email</strong>
                <span class="fs-5">{{ company.email }}</span>
            </div>
            
            <div class="col-12 col-md-6">
                <strong class="d-block mb-1">HR Contact</strong>
                <span class="fs-5">{{ company.hr_contact || 'Not Provided' }}</span>
            </div>

            <div class="col-12 mt-3">
                <strong class="d-block mb-1">Company Website</strong>
                <a v-if="company.website" :href="company.website" target="_blank" class="fs-5 text-decoration-none portal-text-primary">
                    {{ company.website }} ↗
                </a>
                <span v-else class="fs-5 text-muted">Not Provided</span>
            </div>
        </div>

        <div v-if="isAdmin" class="border-top border-dark pt-3 mt-4 d-flex gap-2 justify-content-end">
            <template v-if="company.status === 'PENDING'">
                <button @click="handleAction('approve', company.id)" class="portal-btn portal-btn-success">Approve</button>
                <button @click="handleAction('reject', company.id)" class="portal-btn portal-btn-danger">Reject</button>
            </template>
            <button v-else-if="company.status === 'APPROVED'" @click="handleAction('blacklist', company.id)" class="portal-btn portal-btn-danger">Blacklist Company</button>
            <button v-else-if="company.status === 'BLOCKED'" @click="handleAction('unblock', company.id)" class="portal-btn portal-btn-success">Unblock Company</button>
        </div>
    </section>

    <!-- Sub-component for drives -->
    <CompanyDrives :drives="company.drives" />
  </div>
</template>