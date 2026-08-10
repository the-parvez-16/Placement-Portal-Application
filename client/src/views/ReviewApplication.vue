<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { authState, alertState, navbarState } from '@/store';
import api from '@/services/api';

const route = useRoute();
const applicationId = route.params.id;

const userRole = computed(() => authState.value.role);

// Reactive state matching the DB schema
const application = ref({
    id: applicationId,
    status: 'APPLIED',
    student: {
        name: '',
        email: '',
        branch: '',
        cgpa: null,
        graduation_year: null,
        skills: '',
        resume_file: ''
    },
    drive: {
        job_title: ''
    }
});

const newStatus = ref('');

onMounted(async () => {
    navbarState.value = {
        title: 'Review Application',
        showSearch: false,
        showBackBtn: true,
        backRoute: '' 
    };
    await fetchApplication();
});
const fetchApplication = async () => {
    try {
        const response = await api.get(`/company/applications/${applicationId}`);
        console.log(response.data)
                // Grab the data whether it's an array or an object!
        const data = Array.isArray(response.data) ? response.data[0] : response.data;
        
        application.value = {
            id: data.id || applicationId,
            status: data.status || 'APPLIED',
            student: data.student || {
                name: data.student_name || 'Dummy Student',
                email: 'student@example.com',
                branch: data.student_branch || 'Not Provided',
                cgpa: data.student_cgpa || 8.5,
                graduation_year: 2024,
                skills: 'Python, Vue.js',
                resume_file: ''
            },
            drive: data.drive || {
                job_title: data.drive_title || 'Software Engineer'
            }
        };

    } catch (error) {
        console.error("Failed to load application:", error);
    }
};



const updateStatus = async () => {
    if (!newStatus.value) return;
    
    try {
        console.log(`Updating application ${applicationId} status to ${newStatus.value}`);
        await api.put(`/company/applications/${applicationId}/status`, { status: newStatus.value });

        application.value.status = newStatus.value;
        alertState.value = { type: 'success', message: `Application status updated to ${newStatus.value}!` };
        newStatus.value = ''; 
    } catch (err) {
        console.error(err);
        alertState.value = { type: 'danger', message: 'Failed to update application status.' };
    }
};
</script>

<template>
  <div class="w-100 my-4">
      <div class="row justify-content-center m-0">
          <div class="col-12 col-lg-8">
              <section class="portal-card p-4 mb-4 mt-2">

                  <!-- Header Section -->
                  <div class="border-bottom border-dark pb-3 mb-4 d-flex flex-wrap justify-content-between align-items-center gap-3">
                      <div>
                          <h2 class="fs-4 fw-bold mb-1">{{ application.student.name }}</h2>
                          <span class="fs-6 fw-bold text-muted">Applied for: {{ application.drive.job_title }}</span>
                      </div>
                      <span class="portal-btn" style="pointer-events: none;"
                            :class="{
                                'portal-btn-dark': application.status?.toLowerCase() === 'applied',
                                'portal-btn-primary': application.status?.toLowerCase() === 'shortlisted' || application.status?.toLowerCase() === 'interview',
                                'portal-btn-success': application.status?.toLowerCase() === 'selected',
                                'portal-btn-danger': application.status?.toLowerCase() === 'rejected'
                            }">
                          Status: <span class="text-capitalize">{{ application.status }}</span>
                      </span>
                  </div>

                  <!-- Student Details -->
                  <div class="row mb-4 g-3">
                      <div class="col-12 col-md-6">
                          <strong class="d-block mb-1">Email Address</strong>
                          <span class="fs-5">{{ application.student.email }}</span>
                      </div>
                      <div class="col-12 col-md-6">
                          <strong class="d-block mb-1">Branch</strong>
                          <span class="fs-5">{{ application.student.branch || 'Not provided' }}</span>
                      </div>
                      <div class="col-12 col-md-6">
                          <strong class="d-block mb-1">CGPA</strong>
                          <span class="fs-5">{{ application.student.cgpa || 'N/A' }}</span>
                      </div>
                      <div class="col-12 col-md-6">
                          <strong class="d-block mb-1">Graduation Year</strong>
                          <span class="fs-5">{{ application.student.graduation_year || 'N/A' }}</span>
                      </div>
                      
                      <div class="col-12 mt-3">
                          <strong class="d-block mb-1">Technical & Soft Skills</strong>
                          <span>{{ application.student.skills || 'Not provided' }}</span>
                      </div>
                      
                      <div class="col-12 mt-4">
                          <strong class="d-block mb-2">Resume Document</strong>
                          <a v-if="application.student.resume_file" :href="application.student.resume_file" target="_blank" class="portal-btn portal-btn-dark d-inline-block">
                              View Resume ↗
                          </a>
                          <span v-else class="text-muted fst-italic">No resume uploaded by student.</span>
                      </div>
                  </div>

                  <!-- Action Section -->
                  <div v-if="userRole === 'company'" class="border-top border-dark pt-4 mt-4">
                      <strong class="d-block mb-3 fs-5">Make a Decision</strong>
                      <form @submit.prevent="updateStatus" class="d-flex flex-wrap gap-2 align-items-center mb-0">
                          
                          <!-- Enum ApplicationStatus: APPLIED, SHORTLISTED, INTERVIEW, SELECTED, REJECTED -->
                          <select v-model="newStatus" class="portal-search-input" style="width: 250px;" required>
                              <option value="" disabled>Select new status...</option>
                              <option value="SHORTLISTED">Shortlisted</option>
                              <option value="INTERVIEW">Called for Interview</option>
                              <option value="SELECTED">Final Selection</option>
                              <option value="REJECTED">Rejected</option>
                          </select>
                          
                          <button type="submit" class="portal-btn portal-btn-success" :disabled="!newStatus">
                              Update Status
                          </button>
                      </form>
                  </div>

              </section>
          </div>
      </div>
  </div>
</template>