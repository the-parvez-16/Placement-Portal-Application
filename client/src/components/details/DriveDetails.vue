<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { authState, alertState, navbarState } from '@/store';
import api from '@/services/api';
import { formatDate, formatDateForInput } from '@/utils/formatters';

const route = useRoute();
const drive = ref({});
const alreadyApplied = ref(false); 
const userRole = computed(() => authState.value.role);
const applicationStatus = ref('');

const editForm = ref({});
onMounted(async () => {
    try {
        const driveId = route.params.id;
        const role = authState.value.role;
        const baseUrl = (role === 'admin' || role === 'sudo') ? '/admin' : `/${role}`;
            
        const res = await api.get(`${baseUrl}/drive/${driveId}`);
        drive.value = res.data;
        const editableData = { ...res.data };
        if (editableData.application_deadline) {
            editableData.application_deadline = formatDateForInput(editableData.application_deadline);
        }
        
        editForm.value = editableData;
        if (role === 'student') {
            try {
                const checkRes = await api.get(`/student/drive/${driveId}/check-application`);
                alreadyApplied.value = checkRes.data.applied;
                if (checkRes.data.applied) {
                    applicationStatus.value = checkRes.data.status; 
                }
            } catch (err) {
                console.error("Failed to check application status");
            }
        }

    } catch (err) {
        alertState.value = { type: 'danger', message: 'Failed to load drive details.' };
    }

    navbarState.value = {
        title: 'Drive Details',
        showSearch: false,
        showProfileBtn: true,
        showBackBtn: true
    };
});

const performAction = async (action) => {
    const driveId = route.params.id;
        
    if (action === 'delete' && !confirm('Are you sure you want to delete this drive?')) return;
    if (action === 'reject' && !confirm('Are you sure you want to reject this drive?')) return;
    try {
        if (action === 'apply') {
            try {
                await api.post(`/student/apply/${driveId}`);
                alertState.value = { type: 'success', message: 'Successfully applied to the drive!' };
                alreadyApplied.value = true;
            } catch (err) {
                alertState.value = { 
                    type: 'warning', 
                    message: err.response?.data?.message || 'Please complete your profile before applying!' 
                };
            }
            return;
        } else if (action === 'approve') {
            await api.put(`/admin/drives/${driveId}/status`, { status: "approved" });
            alertState.value = { type: 'success', message: `Drive approved successfully!` };
        } else if (action === 'reject') {
            await api.put(`/admin/drives/${driveId}/status`, { status: "rejected" });
            alertState.value = { type: 'success', message: `Drive rejected successfully!` };
        } else if (action === 'close') {
            await api.put(`/admin/drives/${driveId}/status`, { status: "closed" });
            alertState.value = { type: 'success', message: `Drive closed successfully!` };
        } else if (action === 'delete') {
            alertState.value = { type: 'danger', message: 'Delete not implemented in backend yet!' };
            return;
        }
        const role = authState.value.role;
        const baseUrl = (role === 'admin' || role === 'sudo') ? '/admin' : `/${role}`;
            
        const res = await api.get(`${baseUrl}/drive/${driveId}`);
        drive.value = res.data;
        const editableData = { ...res.data };
        if (editableData.application_deadline) {
            editableData.application_deadline = formatDateForInput(editableData.application_deadline);
        }
        
        editForm.value = editableData;
        
    } catch (err) {
        console.error(err);
        alertState.value = { type: 'danger', message: err.response?.data?.error || 'Action failed.' };
    }
};

const updateDrive = async () => {
    try {
        const driveId = route.params.id;
        await api.put(`/company/drive/${driveId}`, editForm.value);
        
        alertState.value = { type: 'success', message: 'Drive updated successfully!' };
        if (document.activeElement) {
            document.activeElement.blur();
        }
        document.querySelector('#editDriveModal .btn-close').click();
        const res = await api.get(`/company/drive/${driveId}`);
        drive.value = res.data;
        
    } catch (err) {
        alertState.value = { type: 'danger', message: 'Failed to update drive.' };
    }
};
</script>

<template>
  <div class="w-100 my-4">
      <div class="row justify-content-center m-0">
          <div class="col-12 col-lg-8">
              <section class="portal-card p-4 mb-4 mt-2">

                  <div class="border-bottom border-dark pb-3 mb-4 d-flex flex-wrap justify-content-between align-items-center gap-3">
                      <div>
                          <h2 class="fs-4 fw-bold mb-1">{{ drive.job_title }}</h2>
                          <span class="fs-6 fw-bold text-muted">{{ drive.company_name || 'Company Name' }}</span>
                      </div>
                      <span class="portal-btn" style="pointer-events: none;"
                            :class="{
                                'portal-btn-success': drive.status?.toLowerCase() === 'approved',
                                'portal-btn-warning': drive.status?.toLowerCase() === 'pending',
                                'portal-btn-dark': drive.status?.toLowerCase() === 'closed',
                                'portal-btn-danger': drive.status?.toLowerCase() === 'rejected'
                            }">
                          Status: <span class="text-capitalize">{{ drive.status }}</span>
                      </span>
                  </div>

                  <div class="row mb-4 g-3">
                      <div class="col-12 col-md-4">
                          <strong class="d-block mb-1">Salary Package</strong>
                          <span class="fs-5">₹{{ drive.salary || 'Not Specified' }}</span>
                      </div>
                      <div class="col-12 col-md-4">
                          <strong class="d-block mb-1">Minimum CGPA</strong>
                          <span class="fs-5">{{ drive.min_cgpa || 'N/A' }}</span>
                      </div>
                      <div class="col-12 col-md-4">
                          <strong class="d-block mb-1">Allowed Branches</strong>
                          <span class="fs-5">{{ drive.allowed_branches || 'All Branches' }}</span>
                      </div>
                      
                      <div class="col-12 col-md-6 mt-3">
                          <strong class="d-block mb-1">Created At</strong>
                          <span>{{ formatDate(drive.created_at) }}</span>
                      </div>
                      <div class="col-12 col-md-6 mt-3">
                          <strong class="d-block mb-1">Application Deadline</strong>
                          <span>{{ formatDate(drive.application_deadline) }}</span>
                      </div>
                  </div>

                  <div class="mb-4">
                      <strong class="d-block mb-2 border-bottom border-dark pb-1 fs-5">Job Description</strong>
                      <p style="white-space: pre-wrap; font-size: 15px; line-height: 1.6;">{{ drive.job_description }}</p>
                  </div>

                  <div class="d-flex gap-2 border-top border-dark pt-3 mt-4 flex-wrap justify-content-end">
                      <template v-if="userRole === 'company'">
                          <button class="portal-btn portal-btn-primary mb-0" data-bs-toggle="modal" data-bs-target="#editDriveModal">
                              Edit Drive
                          </button>
                          <!-- <button @click="performAction('delete')" class="portal-btn portal-btn-danger mb-0">
                              Delete Drive
                          </button> -->
                      </template>

                      <template v-else-if="userRole === 'admin' || userRole === 'sudo'">
                          <template v-if="drive.status?.toLowerCase() === 'pending'">
                              <button @click="performAction('approve')" class="portal-btn portal-btn-success mb-0">Approve</button>
                              <button @click="performAction('reject')" class="portal-btn portal-btn-danger mb-0">Reject</button>
                          </template>
                          <template v-else-if="drive.status?.toLowerCase() === 'approved'">
                              <button @click="performAction('close')" class="portal-btn portal-btn-success mb-0">Mark as Closed</button>
                          </template>
                      </template>

                      <template v-else-if="userRole === 'student'">
                          <template v-if="drive.status?.toLowerCase() === 'approved'">
                              <button v-if="!alreadyApplied" @click="performAction('apply')" class="portal-btn portal-btn-success mb-0">
                                  Apply Now
                              </button>
                              <span v-else class="portal-btn portal-btn-dark mb-0" style="pointer-events: none;">
                                  Status: <span style="text-transform: capitalize;">{{ applicationStatus }}</span>
                              </span>
                          </template>
                          
                          <span v-else class="portal-btn portal-btn-dark mb-0" style="pointer-events: none;">
                              Applications Closed
                          </span>
                      </template>

                  </div>
              </section>
          </div>
      </div>

      <!-- Edit Modal -->
      <div v-if="userRole === 'company'" class="modal fade" id="editDriveModal" tabindex="-1" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content portal-card" style="border: 2px solid #323232; box-shadow: 6px 6px 0 #323232; background-color: lightgray;">
                  <div class="modal-header border-bottom border-dark">
                      <h5 class="modal-title fw-bold">Edit Placement Drive</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  
                  <form @submit.prevent="updateDrive">
                      <div class="modal-body text-start">
                          <div class="mb-3">
                              <label class="form-label fw-bold">Job Title *</label>
                              <input type="text" v-model="editForm.job_title" class="form-control portal-search-input w-100" required>
                          </div>
                          
                          <div class="row">
                              <div class="col-md-6 mb-3">
                                  <label class="form-label fw-bold">Minimum CGPA *</label>
                                  <input type="number" step="0.01" min="0" max="10" v-model="editForm.min_cgpa" class="form-control portal-search-input w-100" required>
                              </div>
                              <div class="col-md-6 mb-3">
                                  <label class="form-label fw-bold">Allowed Branches *</label>
                                  <input type="text" v-model="editForm.allowed_branches" class="form-control portal-search-input w-100" placeholder="e.g. CSE, ECE" required>
                              </div>
                          </div>

                          <div class="mb-3">
                              <label class="form-label fw-bold">Salary Package</label>
                              <input type="number" v-model="editForm.salary" class="form-control portal-search-input w-100">
                          </div>
                          <div class="mb-3">
                              <label class="form-label fw-bold">Application Deadline</label>
                              <input type="date" v-model="editForm.application_deadline" class="form-control portal-search-input w-100">
                          </div>
                          <div class="mb-3">
                              <label class="form-label fw-bold">Job Description *</label>
                              <textarea v-model="editForm.job_description" class="form-control portal-search-input w-100" style="height: 100px; border-radius: 5px;" required></textarea>
                          </div>
                      </div>
                      <div class="modal-footer border-top border-dark">
                          <button type="button" class="portal-btn portal-btn-dark" data-bs-dismiss="modal">Cancel</button>
                          <button type="submit" class="portal-btn portal-btn-success">Save Changes</button>
                      </div>
                  </form>
              </div>
          </div>
      </div>

  </div>
</template>