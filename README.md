# EvalEval Website
Welcome to the EvalEval Website repository! This is the official website for EvalEval. It serves as a platform for sharing insights, research, and discussions related to evaluation methodologies and related topics.

## Contributing Blog Posts
We welcome contributions from the community!

To pitch a blog post idea, please fill out this form:

👉 [Submit a Blog Idea](https://docs.google.com/forms/d/e/1FAIpQLSeEDHUk2Sx93ffNRqhAjAzeNvlyB98QKOhNr1r96jaXLFdZOQ/viewform)

## 🔧 Updating / Editing the Website
Below are the key folders and files to modify when updating the website:

### `_data/team.yml`
Contains team member info. Entries are listed alphabetically by last name except for hosts.
Sorting is done manually within the yaml file to reduce rendering time in Liquid.

### `_posts/`
Contains blog posts. Templates follow standard Jekyll post structure. 
New posts can be added by duplicating `_posts/2000-01-01-blog-template.md` and updating the front matter and content. You can temporarily hide a post with `published: false`

### `_projects/`
Lists current EvalEval projects.
Clone and edit an existing project file to add a new one.

### `_resources/`
Hosts resource templates (e.g., guides, tutorials).
This section is currently commented out from the navigation bar but can be re-enabled once content is available.

## Navigation Notes
The `/resources` section has been removed from the site’s navigation bar for now in `_includes/navigation.html`, as we don’t yet have content to show. Once we have tutorials or downloadable templates, it can be easily re-added.

## Best Practices
When adding images, use .webp format for better performance and faster load times.
