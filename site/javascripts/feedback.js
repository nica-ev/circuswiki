document.addEventListener('DOMContentLoaded', function() {
  // Function to process the feedback link
  function processFeedbackLink() {
      var feedbackLink = document.querySelector('.md-feedback__note a');

      if (feedbackLink) {
          var pageTitle = document.title;
          var githubUrl = feedbackLink.getAttribute('href').replace('__PAGE_TITLE__', encodeURIComponent(pageTitle));
          feedbackLink.setAttribute('href', githubUrl);
      }
  }

  // Initial processing of the feedback link
  processFeedbackLink();

  // Process the feedback link on content loaded (for PJAX navigation)
  document.addEventListener('pjax:complete', processFeedbackLink); // For older versions of MkDocs Material
  document.addEventListener('contentLoaded', processFeedbackLink);   // For newer versions of MkDocs Material

  var feedback = document.forms.feedback;
  if (feedback) {
      feedback.hidden = false;

      feedback.addEventListener("submit", function(ev) {
          ev.preventDefault();

          var page = document.location.pathname;
          var data = ev.submitter.getAttribute("data-md-value");

          console.log(page, data);

          feedback.firstElementChild.disabled = true;

          var note = feedback.querySelector(
              ".md-feedback__note [data-md-value='" + data + "']"
          );

          if (note) {
              note.hidden = false;
          }

          // Send feedback data to Google Analytics
          if (typeof gtag !== 'undefined') {
              gtag('event', 'feedback', {
                  'page': page,
                  'rating': data
              });
          } else {
              console.warn('Google Analytics gtag not found');
          }
      });
  }
});