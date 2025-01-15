// Function to create remove button
        function createRemoveButton() {
            const button = document.createElement('button');
            button.type = 'button';
            button.className = 'btn btn-sm btn-danger mt-2';
            button.innerHTML = '<i class="bi bi-trash"></i> Remove';
            button.onclick = function() {
                this.closest('.experience-entry, .education-entry').remove();
            };
            return button;
        }
    
        // Add Work Experience
        document.getElementById('addExperience').addEventListener('click', function() {
            const container = document.getElementById('experienceContainer');
            const newEntry = container.children[0].cloneNode(true);
            
            // Clear all input values
            newEntry.querySelectorAll('input, textarea').forEach(input => {
                input.value = '';
            });
            
            // Add remove button
            newEntry.appendChild(createRemoveButton());
            
            container.appendChild(newEntry);
        });
    
        // Add Education
        document.getElementById('addEducation').addEventListener('click', function() {
            const container = document.getElementById('educationContainer');
            const newEntry = container.children[0].cloneNode(true);
            
            // Clear all input values
            newEntry.querySelectorAll('input').forEach(input => {
                input.value = '';
            });
            
            // Add remove button
            newEntry.appendChild(createRemoveButton());
            
            container.appendChild(newEntry);
        });
    
        // Template Selection
        document.querySelectorAll('.template-card').forEach(card => {
            card.addEventListener('click', function() {
                // Remove selected class from all cards
                document.querySelectorAll('.template-card').forEach(c => {
                    c.classList.remove('selected');
                });
                
                // Add selected class to clicked card
                this.classList.add('selected');
                
                // Check the radio button
                this.querySelector('input[type="radio"]').checked = true;
            });
        });
    
        // Form Submission
        document.querySelector('.cv-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Show loading state
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.innerHTML;
            submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Generating...';
            submitButton.disabled = true;
            
            // Here you would typically send the form data to your Django backend
            // For now, we'll just simulate a delay
            setTimeout(() => {
                submitButton.innerHTML = originalText;
                submitButton.disabled = false;
                
                // Show success message (you can customize this based on your needs)
                const alert = document.createElement('div');
                alert.className = 'alert alert-success alert-dismissible fade show';
                alert.innerHTML = `
                    <strong>Success!</strong> Your CV has been generated.
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                `;
                document.querySelector('.main-content').insertBefore(alert, document.querySelector('.profile-overview'));
            }, 2000);
        });
        // Add Language
document.getElementById('addLanguage').addEventListener('click', function() {
    const container = document.getElementById('languageContainer');
    const newEntry = container.children[0].cloneNode(true);
    
    // Clear all input values
    newEntry.querySelectorAll('input, select').forEach(input => {
        input.value = '';
    });
    
    // Add remove button
    newEntry.appendChild(createRemoveButton());
    
    container.appendChild(newEntry);
});

// Add Reference
document.getElementById('addReference').addEventListener('click', function() {
    const container = document.getElementById('referenceContainer');
    const newEntry = container.children[0].cloneNode(true);
    
    // Clear all input values
    newEntry.querySelectorAll('input').forEach(input => {
        input.value = '';
    });
    
    // Add remove button
    newEntry.appendChild(createRemoveButton());
    
    container.appendChild(newEntry);
});
