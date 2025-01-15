// Add this to your static/js/cv-generator.js
document.addEventListener('DOMContentLoaded', function() {
    const cvForm = document.querySelector('.cv-form');
    
    cvForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        try {
            // First get the preview
            const formData = new FormData(cvForm);
            const previewResponse = await fetch('/cv/preview/', {
                method: 'POST',
                body: formData
            });
            
            const previewData = await previewResponse.json();
            
            if (previewData.status === 'success') {
                // Show preview modal
                showPreviewModal(previewData.preview);
            } else {
                alert('Error generating preview: ' + previewData.message);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while generating the preview');
        }
    });
    
    function showPreviewModal(previewImage) {
        // Create modal HTML
        const modalHtml = `
            <div class="modal fade" id="previewModal" tabindex="-1">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">CV Preview</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            <img src="${previewImage}" class="img-fluid" alt="CV Preview">
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-purple" onclick="downloadCV('pdf')">
                                Download PDF
                            </button>
                            <button type="button" class="btn btn-purple" onclick="downloadCV('docx')">
                                Download Word
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        // Add modal to document
        document.body.insertAdjacentHTML('beforeend', modalHtml);
        
        // Show modal
        const modal = new bootstrap.Modal(document.getElementById('previewModal'));
        modal.show();
        
        // Remove modal from DOM after it's hidden
        document.getElementById('previewModal').addEventListener('hidden.bs.modal', function() {
            this.remove();
        });
    }
    
    window.downloadCV = async function(format) {
        try {
            const formData = new FormData(cvForm);
            const response = await fetch(`/cv/download/?format=${format}`, {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                // Create blob and download
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `cv.${format}`;
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                a.remove();
            } else {
                alert('Error downloading CV');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while downloading the CV');
        }
    };
});