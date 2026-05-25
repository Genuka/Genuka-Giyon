from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent


st.set_page_config(
    page_title="Genuka Giyon | Robotics & AI Builder",
    page_icon="GG",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def load_css() -> None:
    css_path = BASE_DIR / "styles.css"
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def asset(path: str) -> Path:
    return BASE_DIR / "assets" / path


def media_exists(path: str) -> bool:
    return asset(path).exists()


def image_or_placeholder(path: str, label: str, caption: str = "") -> None:
    full_path = asset(path)
    if full_path.exists():
        st.image(str(full_path), caption=caption or label, use_container_width=True)
    else:
        st.markdown(
            f"""
            <div class="media-placeholder">
              <div class="placeholder-grid"></div>
              <span>{label}</span>
              <small>{path}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )


def download_if_available(path: str, label: str) -> None:
    full_path = BASE_DIR / path
    if full_path.exists():
        st.download_button(
            label=label,
            data=full_path.read_bytes(),
            file_name=full_path.name,
            mime="application/pdf",
            use_container_width=True,
        )


def metric(label: str, value: str, detail: str = "") -> str:
    return f"""
    <div class="metric">
      <span>{label}</span>
      <strong>{value}</strong>
      <small>{detail}</small>
    </div>
    """


def tag(text: str) -> str:
    return f"<span class='tag'>{text}</span>"


def status_chip(text: str, kind: str = "default") -> str:
    return f"<span class='status status-{kind}'>{text}</span>"


load_css()

PROJECTS = [
    {
        "title": "ICIA Greenhouse Temperature Controller",
        "kicker": "International Bronze - ICIA 2025 Vietnam",
        "status": "Featured",
        "summary": (
            "A fully off-grid greenhouse climate control system built solo with an ESP32, "
            "solar power, relays, battery support, LCD feedback, fans, and temperature/humidity control."
        ),
        "story": (
            "This project was built under pressure for an international competition, with sustainability "
            "and embedded systems at the center. It represented Sri Lanka after national selection and won "
            "bronze at ICIA 2025 in Vietnam."
        ),
        "tags": ["ESP32", "Solar", "Relays", "LCD", "Humidity", "Temperature", "Embedded Systems"],
        "image": "images/projects/icia-greenhouse/icia-medal-certificate-vietnam.png",
        "downloads": [
            ("Download bronze certificate", "assets/images/certificates/icia/icia-2025-bronze-certificate.pdf"),
            ("Download national selection certificate", "assets/images/certificates/icia/icia-2025-national-selection.pdf"),
        ],
    },
    {
        "title": "AI Smart Attendance System",
        "kicker": "Computer Vision - Live Dashboard",
        "status": "Featured",
        "summary": (
            "A live attendance intelligence system using face recognition, image recognition, YOLO, "
            "OpenCV, PyTorch, a custom model, and a Flask web dashboard."
        ),
        "story": (
            "The system tracked who was inside, who had arrived, who was still missing, total capacity, "
            "arrival times, and departure events. When the cameras failed before demonstration, the system "
            "had to be recovered fast under pressure."
        ),
        "tags": ["PyTorch", "YOLO", "OpenCV", "Flask", "HTML/CSS", "Computer Vision", "Dashboard"],
        "image": "images/projects/ai-attendance/ai-attendance-dashboard.png",
        "video": "images/projects/ai-attendance/ai-attendance-demo.mp4",
        "downloads": [],
    },
    {
        "title": "SLIT Robofest Line Follower",
        "kicker": "Competition Robot - 2024",
        "status": "Archive",
        "summary": (
            "An ESP32 line follower using N20 motors, an 8-sensor array, L293D motor driver, "
            "PID tuning, threshold logic, and a fully 3D-designed chassis."
        ),
        "story": (
            "Built for speed, efficiency, and precise motion control. The project strengthened practical "
            "robotics skills across sensors, motors, chassis design, and control tuning."
        ),
        "tags": ["ESP32", "N20 Motors", "8-Sensor Array", "L293D", "PID", "3D Design"],
        "image": "images/projects/robofest-line-follower/robofest-line-follower-01.jpg",
        "downloads": [],
    },
    {
        "title": "Image-to-Drawing CNC Plotter",
        "kicker": "Future Build - Concept",
        "status": "In Progress",
        "summary": (
            "A CNC-style drawing machine concept that will convert uploaded images into physical drawings "
            "using stepper motors and path-generation software."
        ),
        "story": (
            "This future project will connect computer vision, mechanical motion, and machine control into "
            "a physical creative system."
        ),
        "tags": ["Stepper Motors", "CNC", "Image Processing", "Mechanical Design", "In Progress"],
        "image": "images/projects/cnc-drawing-machine/cnc-drawing-concept-01.jpg",
        "downloads": [],
    },
]

SKILLS = {
    "AI + Vision": ["PyTorch", "TensorFlow", "OpenCV", "YOLO", "Edge Impulse", "LLM APIs"],
    "Robotics": ["ESP32", "Arduino", "Raspberry Pi", "Sensors", "Motors", "Servos", "Relays"],
    "Engineering": ["PCB basics", "Solar systems", "Embedded control", "Mechanical prototyping"],
    "Design + Web": ["HTML", "CSS", "Flask", "Streamlit", "Fusion 360", "Tinkercad", "Blender learning"],
    "Tools": ["VS Code", "Git", "GitHub", "Windows", "Arduino IDE"],
}

TIMELINE = [
    ("2012", "Born", "Young robotics and AI builder from Kadawatha, Gampaha, Sri Lanka."),
    ("Grade 1-8", "Yoshida Shokanji International School", "Built strong early academic foundations."),
    ("Grade 1-5/6", "Class First", "Placed first in class through early school years."),
    ("2024", "SLIT Robofest", "Built an ESP32 line follower with custom control logic and 3D-designed chassis."),
    ("2025", "ICIA Vietnam Bronze", "Nationally selected and won bronze for an off-grid greenhouse controller."),
    ("2026", "O/L Path", "English, Biology, Chemistry, Physics, Mathematics, Computer Science, and French."),
    ("2027", "A/L Direction", "Continuing toward advanced engineering, robotics, and AI systems."),
]


st.markdown(
    """
    <div class="top-nav">
      <div class="brand-mark">GG</div>
      <div class="nav-links">
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#timeline">Timeline</a>
        <a href="#contact">Contact</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_left, hero_right = st.columns([1.08, 0.92], gap="large")

with hero_left:
    st.markdown(
        """
        <section class="hero">
          <div class="eyebrow">Born 2012 - Young Robotics & AI Builder</div>
          <h1>Genuka Giyon</h1>
          <p class="hero-line">Building intelligent machines for the physical world and a cleaner future.</p>
          <p class="hero-copy">
            A creative, competitive systems thinker building robotics, AI vision systems, embedded hardware,
            and engineering experiments with real-world purpose.
          </p>
          <div class="hero-actions">
            <a class="primary-action" href="#projects">View featured systems</a>
            <a class="secondary-action" href="https://github.com/Genuka" target="_blank">GitHub</a>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown(
        """
        <div class="system-orb" aria-label="Abstract robotics and AI visual">
          <div class="orb-core"></div>
          <div class="orbit orbit-one"></div>
          <div class="orbit orbit-two"></div>
          <div class="orbit orbit-three"></div>
          <div class="node node-a"></div>
          <div class="node node-b"></div>
          <div class="node node-c"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <section class="stat-band">
      {metric("International", "Bronze", "ICIA 2025 Vietnam")}
      {metric("Focus", "Robotics + AI", "Physical-world systems")}
      {metric("Build Style", "Solo Maker", "Fast under pressure")}
      {metric("Mission", "Cleaner Future", "Useful systems for humans")}
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<section class="section" id="about">', unsafe_allow_html=True)
about_left, about_right = st.columns([0.9, 1.1], gap="large")
with about_left:
    image_or_placeholder("images/profile/genuka-profile.jpg", "Profile image placeholder")
with about_right:
    st.markdown(
        """
        <div class="section-kicker">About</div>
        <h2 class="section-title">A builder focused on machines that actually work.</h2>
        <p class="body-large">
          I want to build things, see them work, and use engineering to make life easier for humans while
          helping the planet. My direction is robotics, AI systems, embedded control, computer vision,
          and physical machines that solve real problems.
        </p>
        <p class="body-large">
          I do not want a future where engineering is only sitting at a desk. I want to design, test,
          tune, move around, prototype, and build systems that can keep scaling with me over the years.
        </p>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</section>", unsafe_allow_html=True)

st.markdown('<section class="section" id="projects">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-kicker">Featured Work</div>
    <h2 class="section-title">Real systems, pressure-tested builds.</h2>
    """,
    unsafe_allow_html=True,
)

for index, project in enumerate(PROJECTS):
    left, right = st.columns([0.92, 1.08], gap="large")
    media_col, text_col = (left, right) if index % 2 == 0 else (right, left)
    with media_col:
        image_or_placeholder(project["image"], project["title"])
        if project.get("video") and media_exists(project["video"]):
            st.video(str(asset(project["video"])))
    with text_col:
        chips = status_chip(project["status"], "featured" if project["status"] == "Featured" else "default")
        tags = "".join(tag(item) for item in project["tags"])
        st.markdown(
            f"""
            <article class="project-card">
              <div class="project-topline">
                <span>{project["kicker"]}</span>
                {chips}
              </div>
              <h3>{project["title"]}</h3>
              <p class="project-summary">{project["summary"]}</p>
              <p>{project["story"]}</p>
              <div class="tag-row">{tags}</div>
              <div class="project-links"><span class='muted-note'>Media, repositories, and live demos can be added as the project grows.</span></div>
            </article>
            """,
            unsafe_allow_html=True,
        )
        for label, path in project.get("downloads", []):
            download_if_available(path, label)
    if project["title"].startswith("ICIA"):
        st.markdown(
            """
            <div class="diagram">
              <span>Solar Panel</span>
              <b></b>
              <span>Battery</span>
              <b></b>
              <span>ESP32</span>
              <b></b>
              <span>Sensors</span>
              <b></b>
              <span>Relay + Fans</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    if project["title"].startswith("AI"):
        st.markdown(
            """
            <div class="diagram">
              <span>Camera</span>
              <b></b>
              <span>OpenCV</span>
              <b></b>
              <span>YOLO + PyTorch</span>
              <b></b>
              <span>Recognition</span>
              <b></b>
              <span>Flask Dashboard</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("</section>", unsafe_allow_html=True)

st.markdown('<section class="section" id="skills">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-kicker">Capabilities</div>
    <h2 class="section-title">A stack built around robotics, AI, and real hardware.</h2>
    """,
    unsafe_allow_html=True,
)
skill_columns = st.columns(5, gap="medium")
for column, (group, items) in zip(skill_columns, SKILLS.items()):
    with column:
        st.markdown(
            f"""
            <div class="skill-card">
              <h3>{group}</h3>
              <p>{", ".join(items)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
st.markdown("</section>", unsafe_allow_html=True)

st.markdown('<section class="section" id="timeline">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-kicker">Timeline</div>
    <h2 class="section-title">Early path, serious trajectory.</h2>
    <div class="timeline">
    """,
    unsafe_allow_html=True,
)
for year, title, detail in TIMELINE:
    st.markdown(
        f"""
        <div class="timeline-item">
          <span>{year}</span>
          <div>
            <h3>{title}</h3>
            <p>{detail}</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div></section>", unsafe_allow_html=True)

st.markdown('<section class="section" id="credentials">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-kicker">Credentials</div>
    <h2 class="section-title">Certificates and proof, ready for upload.</h2>
    <p class="body-large">Add the certificate files using the exact names below and the portfolio will link to them.</p>
    <div class="credential-grid">
      <div class="credential-card"><strong>ICIA Bronze</strong><span>assets/images/certificates/icia/icia-2025-bronze-certificate.pdf</span></div>
      <div class="credential-card"><strong>ICIA National Selection</strong><span>assets/images/certificates/icia/icia-2025-national-selection.pdf</span></div>
      <div class="credential-card"><strong>Meu Labs Certificate 01</strong><span>assets/images/certificates/meu-labs/meu-labs-certificate-01.pdf</span></div>
      <div class="credential-card"><strong>Meu Labs Certificate 02</strong><span>assets/images/certificates/meu-labs/meu-labs-certificate-02.pdf</span></div>
      <div class="credential-card"><strong>Meu Labs Certificate 03</strong><span>assets/images/certificates/meu-labs/meu-labs-certificate-03.pdf</span></div>
      <div class="credential-card"><strong>Meu Labs Certificate 04</strong><span>assets/images/certificates/meu-labs/meu-labs-certificate-04.pdf</span></div>
      <div class="credential-card"><strong>Meu Labs Certificate 05</strong><span>assets/images/certificates/meu-labs/meu-labs-certificate-05.pdf</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)
certificate_downloads = [
    ("Download ICIA bronze certificate", "assets/images/certificates/icia/icia-2025-bronze-certificate.pdf"),
    ("Download ICIA national selection certificate", "assets/images/certificates/icia/icia-2025-national-selection.pdf"),
    ("Download Meu Labs certificate 01", "assets/images/certificates/meu-labs/meu-labs-certificate-01.pdf"),
    ("Download Meu Labs certificate 02", "assets/images/certificates/meu-labs/meu-labs-certificate-02.pdf"),
    ("Download Meu Labs certificate 03", "assets/images/certificates/meu-labs/meu-labs-certificate-03.pdf"),
    ("Download Meu Labs certificate 04", "assets/images/certificates/meu-labs/meu-labs-certificate-04.pdf"),
    ("Download Meu Labs certificate 05", "assets/images/certificates/meu-labs/meu-labs-certificate-05.pdf"),
]
download_columns = st.columns(2, gap="medium")
for index, (label, path) in enumerate(certificate_downloads):
    with download_columns[index % 2]:
        download_if_available(path, label)
st.markdown("</section>", unsafe_allow_html=True)

st.markdown('<section class="section contact-section" id="contact">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-kicker">Contact</div>
    <h2 class="section-title">Building toward robotics, AI systems, and deep-tech work.</h2>
    <div class="contact-grid">
      <a href="mailto:genuakgiyon@gmail.com">genuakgiyon@gmail.com</a>
      <a href="tel:+94712373765">+94 71 237 3765</a>
      <a href="https://github.com/Genuka" target="_blank">github.com/Genuka</a>
      <a href="https://instagram.com/genukagiyon" target="_blank">@genukagiyon</a>
      <span>LinkedIn coming soon</span>
      <span>Kadawatha, Gampaha, Sri Lanka</span>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</section>", unsafe_allow_html=True)

st.markdown(
    """
    <button class="sound-toggle" onclick="this.classList.toggle('muted')">Sound: subtle</button>
    <script>
      const button = window.parent.document.querySelector('.sound-toggle');
    </script>
    """,
    unsafe_allow_html=True,
)
