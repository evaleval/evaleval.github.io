---
title: Organizers
nav: true
---

<style>
.organizer-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}
.lead-organizer-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  margin-bottom: 2em;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}
.core-organizer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 2em;
}
/* Add styles to center the last row when there's an incomplete number of items */
.core-organizer-grid::after {
  content: "";
  grid-column: span 2;
}
.organizer-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.lead-organizer-grid .organizer-photo {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 15px;
}
.core-organizer-grid .organizer-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}
.organizer-info {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.section-card {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 20px 30px;
  margin-top: 40px;
  margin-bottom: 40px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
h1 {
  margin-bottom: 0.5em;
}
h2 {
  margin-top: 1em;
  margin-bottom: 0.5em;
}
a {
  color: #0366d6;
}
@media (max-width: 768px) {
  .lead-organizer-grid {
    grid-template-columns: 1fr;
  }
  .core-organizer-grid {
    grid-template-columns: 1fr;
  }
  .core-organizer-grid::after {
    content: none;
  }
}
.section-card + h1, 
.section-card + h2 {
  margin-top: 3em;
}
</style>

# Lead Organizers

<div class="section-card">
<div class="lead-organizer-grid">
  <div class="organizer-card">
    <img src="images/avijit-ghosh.jpg" alt="Avijit Ghosh" class="organizer-photo">
    <div class="organizer-info">
      <strong>Avijit Ghosh</strong>
      <span>Applied Policy Researcher, Hugging Face</span>
      <a href="mailto:avijit@huggingface.co">avijit@huggingface.co</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/irene-solaiman.jpg" alt="Irene Solaiman" class="organizer-photo">
    <div class="organizer-info">
      <strong>Irene Solaiman</strong>
      <span>Head of Global Policy, Hugging Face</span>
      <a href="mailto:irene@huggingface.co">irene@huggingface.co</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/zeerak-talat.jpg" alt="Zeerak Talat" class="organizer-photo">
    <div class="organizer-info">
      <strong>Zeerak Talat</strong>
      <span>Research Fellow, MBZUAI</span>
      <a href="mailto:z@zeerak.org">z@zeerak.org</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/yacine-jernite.jpg" alt="Yacine Jernite" class="organizer-photo">
    <div class="organizer-info">
      <strong>Yacine Jernite</strong>
      <span>Machine Learning and Society Lead, Hugging Face</span>
      <a href="mailto:yacine@huggingface.co">yacine@huggingface.co</a>
    </div>
  </div>
</div>
</div>

# Core Organizers

<div class="section-card">
<div class="core-organizer-grid">
  <div class="organizer-card">
    <img src="images/usman-gohar.jpg" alt="Usman Gohar" class="organizer-photo">
    <div class="organizer-info">
      <strong>Usman Gohar</strong>
      <span>Ph.D. student, Iowa State University</span>
      <a href="mailto:ugohar@iastate.edu">ugohar@iastate.edu</a>
    </div>
  </div>  
  <div class="organizer-card">
    <img src="images/jennifer-mickel.jpg" alt="Jennifer Mickel" class="organizer-photo">
    <div class="organizer-info">
      <strong>Jennifer Mickel</strong>
      <span>Researcher in AI and algorithmic fairness</span>
      <a href="mailto:jamickel@utexas.edu">jamickel@utexas.edu</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/lucie-aimee-kaffee.jpg" alt="Lucie-Aimée Kaffee" class="organizer-photo">
    <div class="organizer-info">
      <strong>Lucie-Aimée Kaffee</strong>
      <span>Applied Policy Researcher, Hugging Face</span>
      <a href="mailto:lucie.kaffee@huggingface.co">lucie.kaffee@huggingface.co</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/arjun-subramonian.jpg" alt="Arjun Subramonian" class="organizer-photo">
    <div class="organizer-info">
      <strong>Arjun Subramonian</strong>
      <span>Computer Science PhD candidate, UCLA</span>
      <a href="mailto:arjunsub@cs.ucla.edu">arjunsub@cs.ucla.edu</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/alberto-lusoli.jpg" alt="Alberto Lusoli" class="organizer-photo">
    <div class="organizer-info">
      <strong>Alberto Lusoli</strong>
      <span>Digital Democracies Institute Deputy Director, Simon Fraser University</span>
      <a href="mailto:alberto.lusoli@gmail.com">alberto.lusoli@gmail.com</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/felix-friedrich.jpg" alt="Felix Friedrich" class="organizer-photo">
    <div class="organizer-info">
      <strong>Felix Friedrich</strong>
      <span>PhD student, TU Darmstadt & hessian.AI</span>
      <a href="mailto:friedrich@cs.tu-darmstadt.de">friedrich@cs.tu-darmstadt.de</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/cedric-whitney.jpg" alt="Cedric Whitney" class="organizer-photo">
    <div class="organizer-info">
      <strong>Cedric Whitney</strong>
      <span>University of California, Berkeley</span>
      <a href="mailto:cedric@ischool.berkeley.edu">cedric@ischool.berkeley.edu</a>
    </div>
  </div>
  <div class="organizer-card">
    <img src="images/michelle-lin.jpg" alt="Michelle Lin" class="organizer-photo">
    <div class="organizer-info">
      <strong>Michelle Lin</strong>
      <span>Mila Quebec AI Institute</span>
      <a href="mailto:michelle.lin2@mail.mgcill.ca">michelle.lin2@mail.mgcill.ca</a>
    </div>
  </div>
</div>
</div>

# Additional Contributors

<div class="section-card" markdown="1">

- William Agnew (University of Washington)
- Lama Ahmad (OpenAI)
- Dylan Baker (DAIR)
- Canyu Chen (Illinois Institute of Technology)
- Hal Daumé III (University of Maryland)
- Jesse Dodge (Allen Institute for AI)
- Isabella Duan (University of Chicago)
- Ellie Evans (Independent)
- Sara Hooker (Cohere for AI)
- Ria Kalluri (Stanford University)
- Alina Leidinger (University of Amsterdam)
- Xiuzhu Lin (Independent)
- Sasha Luccioni (Hugging Face)
- Margaret Mitchell (Hugging Face)
- Jessica Newman (University of California, Berkeley)
- Anaelia Ovalle (University of California, Los Angeles)
- Marie-Therese Png (Oxford University)
- Levent Sagun (Independent)
- Shubham Singh (University of Illinois Chicago)
- Andrew Strait (Ada Lovelace)
- Lukas Struppek (German Center for Artificial Intelligence, TU Darmstadt)

</div>


# Acknowledgments

<div class="section-card">

We gratefully acknowledge the support of all our organizers, additional contributors, and the NeurIPS community in making this workshop possible.
</div>
