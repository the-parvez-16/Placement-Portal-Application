<script setup>
import { ref } from 'vue';
import api from "@/services/api";
import { alertState } from '@/store';

const driveData = ref({
    jobTitle: '',
    minCgpa: '',
    allowedBranches: '',
    salary: '',
    applicationDeadline: '',
    jobDescription: ''
});

const submitDrive = async () => {
    try {
        const payload = {
            job_title: driveData.value.jobTitle,
            job_description: driveData.value.jobDescription,
            min_cgpa: parseFloat(driveData.value.minCgpa) || null,
            allowed_branches: driveData.value.allowedBranches || null,
            salary: parseInt(driveData.value.salary) || null,
            application_deadline: driveData.value.applicationDeadline || null
        };
        await api.post('/company/drives', payload);
        alertState.value = { type: 'success', message: 'Drive created successfully! Refresh to see it.' };
    } catch (err) {
        alertState.value = { type: 'danger', message: 'Failed to create drive.' };
    }
};
</script>

<template>
    <div class="modal fade" id="createDriveModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content portal-card" style="border: 2px solid #323232; box-shadow: 6px 6px 0 #323232; background-color: #f1f3f5;">
                
                <div class="modal-header border-bottom border-dark">
                    <h5 class="modal-title fw-bold">Create New Placement Drive</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                
                <form @submit.prevent="submitDrive">
                    <div class="modal-body">
                        <div class="mb-3">
                            <label class="form-label fw-bold">Job Title *</label>
                            <input v-model="driveData.jobTitle" type="text" class="form-control portal-search-input w-100" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-bold">Minimum CGPA</label>
                            <input v-model="driveData.minCgpa" type="number" step="0.1" class="form-control portal-search-input w-100" placeholder="e.g. 7.5">
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-bold">Allowed Branches</label>
                            <input v-model="driveData.allowedBranches" type="text" class="form-control portal-search-input w-100" placeholder="e.g. CSE, ECE, ME">
                        </div>

                        <div class="mb-3">
                            <label class="form-label fw-bold">Salary (Optional)</label>
                            <input v-model="driveData.salary" type="number" class="form-control portal-search-input w-100" placeholder="e.g. ₹500000">
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-bold">Application Deadline</label>
                            <input v-model="driveData.applicationDeadline" type="date" class="form-control portal-search-input w-100">
                        </div>
                        <div class="mb-3">
                            <label class="form-label fw-bold">Job Description *</label>
                            <textarea v-model="driveData.jobDescription" class="form-control portal-search-input w-100" style="height: 100px; border-radius: 5px;" required></textarea>
                        </div>
                    </div>
                    
                    <div class="modal-footer border-top border-dark">
                        <button type="button" class="portal-btn portal-btn-dark" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="portal-btn portal-btn-primary">Submit Drive</button>
                    </div>
                </form>

            </div>
        </div>
    </div>
</template>