<script setup>
import { ref } from 'vue';

const driveData = ref({
    jobTitle: '',
    eligibilityCriteria: '',
    salary: '',
    applicationDeadline: '',
    jobDescription: ''
});

const submitDrive = () => {
    console.log("Submitting Drive:", driveData.value);
    // Yahan API call aayegi drive create karne ke liye
    // Uske baad programmatic modal close aur toast message
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
                            <label class="form-label fw-bold">Eligibility Criteria *</label>
                            <input v-model="driveData.eligibilityCriteria" type="text" class="form-control portal-search-input w-100" placeholder="e.g. B.Tech CS, 7+ CGPA" required>
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