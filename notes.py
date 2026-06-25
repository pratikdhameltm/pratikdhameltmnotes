
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os, html

# ------------ Output file ------------
out_path = "DevOps_Interview_QA.pdf"

# ------------ Styles ------------
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle", parent=styles["Title"],
    fontName="Helvetica-Bold", fontSize=26, textColor=colors.HexColor("#0B3D91"),
    alignment=TA_CENTER, spaceAfter=12
)
subtitle_style = ParagraphStyle(
    "SubtitleStyle", parent=styles["Normal"],
    fontName="Helvetica-Oblique", fontSize=13, textColor=colors.HexColor("#444444"),
    alignment=TA_CENTER, spaceAfter=20
)
section_style = ParagraphStyle(
    "SectionStyle", parent=styles["Heading1"],
    fontName="Helvetica-Bold", fontSize=17, textColor=colors.white,
    backColor=colors.HexColor("#0B3D91"), borderPadding=(6,6,6,6),
    spaceBefore=14, spaceAfter=10, leading=22
)
question_style = ParagraphStyle(
    "QuestionStyle", parent=styles["Normal"],
    fontName="Helvetica-Bold", fontSize=11.5, textColor=colors.HexColor("#1F2937"),
    spaceBefore=8, spaceAfter=3, leading=14
)
answer_style = ParagraphStyle(
    "AnswerStyle", parent=styles["Normal"],
    fontName="Helvetica", fontSize=10.5, textColor=colors.HexColor("#222222"),
    spaceAfter=6, leading=14, alignment=TA_LEFT
)
code_style = ParagraphStyle(
    "CodeStyle", parent=styles["Code"],
    fontName="Courier", fontSize=9.5, textColor=colors.HexColor("#0B3D91"),
    backColor=colors.HexColor("#F1F3F5"), leftIndent=8, rightIndent=8,
    spaceBefore=4, spaceAfter=8, leading=12
)
bullet_style = ParagraphStyle(
    "Bullet", parent=answer_style, leftIndent=14, bulletIndent=4, spaceAfter=2
)

def P(txt, style=answer_style):
    return Paragraph(txt, style)

def Q(num, text):
    return Paragraph(f"Q{num}. {html.escape(text)}", question_style)

def A(text):
    return Paragraph(text, answer_style)

def Code(text):
    safe = html.escape(text).replace("\n", "<br/>")
    return Paragraph(safe, code_style)

def Section(name):
    return Paragraph(name, section_style)

def Bullets(items):
    return [Paragraph(f"&bull;&nbsp; {it}", bullet_style) for it in items]

# ------------ Content ------------
story = []

# Title page
story.append(Spacer(1, 4*cm))
story.append(P("DevOps Interview — Consolidated Q&A", title_style))
story.append(P("Deduplicated • Interview-Ready • Quick Revision Sheet", subtitle_style))
story.append(Spacer(1, 1*cm))

toc = [
    "1.  Linux Commands & Concepts",
    "2.  Docker",
    "3.  Kubernetes",
    "4.  Jenkins",
    "5.  Terraform",
    "6.  Ansible",
    "7.  Git & GitHub",
    "8.  AWS",
    "9.  CI/CD & General",
]
story.append(P("<b>Table of Contents</b>", ParagraphStyle("toc", parent=answer_style, fontSize=13, alignment=TA_CENTER, spaceAfter=10)))
for t in toc:
    story.append(P(t, ParagraphStyle("tocitem", parent=answer_style, fontSize=11.5, alignment=TA_CENTER, spaceAfter=3)))
story.append(PageBreak())

# ============ 1. LINUX ============
story.append(Section("1. Linux Commands & Concepts"))

story.append(Q(1, "What is sudo and why is it used?"))
story.append(A("<b>sudo</b> (Superuser Do) executes a command with root/administrative privileges. Used to install packages, edit system files, or manage services that a normal user can't perform."))

story.append(Q(2, "Difference between ll and ls -a (and ls)"))
story.extend(Bullets([
    "<b>ls</b> → lists files/directories.",
    "<b>ls -a</b> → lists all files including hidden ones (starting with '.').",
    "<b>ll</b> → alias for <b>ls -l</b>, long listing (permissions, owner, size, date).",
]))

story.append(Q(3, "Top 10 Linux commands"))
story.append(A("ls, cd, pwd, cp, mv, rm, cat, grep, chmod, ps, top, df, tar, ssh, sudo."))

story.append(Q(4, "How to kill a process?"))
story.append(Code("ps -ef | grep <process>     # find PID\nkill <PID>                  # graceful\nkill -9 <PID>               # force kill\npkill <name>                # by name"))

story.append(Q(5, "How to check memory / CPU / disk usage?"))
story.extend(Bullets([
    "Memory → <b>free -h</b>, <b>top</b>",
    "CPU → <b>top</b>, <b>htop</b>, <b>mpstat</b>",
    "Disk free → <b>df -h</b>",
    "Directory size → <b>du -sh *</b>",
]))

story.append(Q(6, "ping command"))
story.append(A("Sends ICMP packets to test network reachability and latency to a host."))

story.append(Q(7, "curl command"))
story.append(A("Transfers data to/from a server (HTTP, HTTPS, FTP). Used to test APIs or download files: <font face='Courier'>curl -O https://url/file</font>."))

story.append(Q(8, "How to download a file from the internet via CLI?"))
story.append(Code("wget <url>\ncurl -O <url>"))

story.append(Q(9, "chmod command"))
story.append(A("Changes file permissions. e.g. <font face='Courier'>chmod 755 file.sh</font> → rwxr-xr-x."))

story.append(Q(10, "top command"))
story.append(A("Real-time view of running processes, CPU, memory, and load average."))

story.append(Q(11, "cat command"))
story.append(A("Displays file contents, concatenates files, or creates new files."))

story.append(Q(12, "How to compress a file?"))
story.append(Code("tar -czvf archive.tar.gz folder/\nzip archive.zip file"))

story.append(Q(13, "Command to check open ports"))
story.append(Code("netstat -tulnp\nss -tulnp"))

story.append(PageBreak())

# ============ 2. DOCKER ============
story.append(Section("2. Docker"))

story.append(Q(14, "What is Docker Compose?"))
story.append(A("A tool to define and run multi-container Docker apps using a single <font face='Courier'>docker-compose.yml</font> file. Brings up the whole stack with <font face='Courier'>docker compose up</font>."))

story.append(Q(15, "What is Docker Expose?"))
story.append(A("<b>EXPOSE</b> in a Dockerfile <i>documents</i> which port the container listens on. It does NOT publish it — <font face='Courier'>-p</font> does that at runtime."))

story.append(Q(16, "CMD vs ENTRYPOINT"))
story.extend(Bullets([
    "<b>CMD</b> → default arguments; can be overridden at <font face='Courier'>docker run</font>.",
    "<b>ENTRYPOINT</b> → fixed executable; CMD args append to it.",
    "Best practice: ENTRYPOINT for binary, CMD for default args.",
]))

story.append(Q(17, "Docker RUN instruction"))
story.append(A("Executes a command during image build and commits the result as a new layer (e.g., <font face='Courier'>RUN apt-get install -y nginx</font>)."))

story.append(Q(18, "Components of a Dockerfile"))
story.append(A("FROM, LABEL, RUN, COPY/ADD, WORKDIR, ENV, EXPOSE, CMD, ENTRYPOINT, VOLUME, USER."))

story.append(Q(19, "Types of Docker networks (default = bridge)"))
story.extend(Bullets([
    "<b>bridge</b> (default for standalone containers)",
    "<b>host</b> (shares host network)",
    "<b>none</b> (no network)",
    "<b>overlay</b> (multi-host, with Swarm)",
    "<b>macvlan</b> (assigns MAC address)",
]))

story.append(Q(20, "How to expose a port in Docker?"))
story.extend(Bullets([
    "In Dockerfile: <font face='Courier'>EXPOSE 8080</font>",
    "At runtime: <font face='Courier'>docker run -p 8080:8080 image</font>",
]))

story.append(Q(21, "ECR vs DockerHub"))
tbl = Table(
    [["ECR", "DockerHub"],
     ["AWS-managed private registry", "Public/private registry by Docker Inc."],
     ["IAM-based authentication", "Username/password / token"],
     ["Native AWS integration (EKS, ECS)", "Universal, easy public sharing"]],
    colWidths=[8*cm, 8*cm]
)
tbl.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0), colors.HexColor("#0B3D91")),
    ("TEXTCOLOR",(0,0),(-1,0), colors.white),
    ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
    ("ALIGN",(0,0),(-1,-1),"LEFT"),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("GRID",(0,0),(-1,-1),0.4,colors.grey),
    ("FONTSIZE",(0,0),(-1,-1),10),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("RIGHTPADDING",(0,0),(-1,-1),6),
    ("TOPPADDING",(0,0),(-1,-1),4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
]))
story.append(tbl)
story.append(Spacer(1, 0.3*cm))

story.append(Q(22, "docker run vs docker start"))
story.extend(Bullets([
    "<b>docker run</b> → creates a NEW container from an image.",
    "<b>docker start</b> → restarts an EXISTING stopped container.",
]))

story.append(Q(23, "docker ps"))
story.append(A("Lists running containers. <font face='Courier'>docker ps -a</font> lists all."))

story.append(Q(24, "docker inspect"))
story.append(A("Returns detailed JSON metadata (IP, mounts, env, network) for a container/image."))

story.append(Q(25, "docker prune"))
story.append(A("Removes unused data — stopped containers, dangling images, unused networks/volumes. <font face='Courier'>docker system prune -a</font> cleans everything unused."))

story.append(Q(26, "Common Docker commands"))
story.append(A("build, run, ps, images, pull, push, exec, logs, stop, rm, rmi, network, volume, inspect."))

story.append(Q(27, "Docker vs Kubernetes"))
story.append(A("Docker → containerization platform. Kubernetes → orchestrator managing many containers across clusters (scaling, healing, networking)."))

story.append(PageBreak())

# ============ 3. KUBERNETES ============
story.append(Section("3. Kubernetes"))

story.append(Q(28, "Kubernetes Architecture"))
story.append(A("<b>Control Plane:</b> API Server, etcd, Scheduler, Controller Manager, Cloud Controller Manager.<br/><b>Worker Node:</b> kubelet, kube-proxy, Container Runtime (containerd)."))

story.append(Q(29, "What is a Pod?"))
story.append(A("Smallest deployable unit in K8s — one or more containers sharing network and storage."))

story.append(Q(30, "Types of K8s Services"))
story.extend(Bullets([
    "<b>ClusterIP</b> (default, internal)",
    "<b>NodePort</b> (exposes on node IP:port)",
    "<b>LoadBalancer</b> (cloud LB)",
    "<b>ExternalName</b> (DNS alias)",
]))

story.append(Q(31, "Significance of LoadBalancer service"))
story.append(A("Provisions a cloud LB that distributes external traffic across pods — single stable endpoint for users."))

story.append(Q(32, "How to expose NodePort publicly?"))
story.append(A("Open NodePort range (30000–32767) in node's security group, then access via <font face='Courier'>&lt;NodeIP&gt;:&lt;NodePort&gt;</font>."))

story.append(Q(33, "HPA vs VPA"))
story.extend(Bullets([
    "<b>HPA</b> → adds/removes pods based on metrics.",
    "<b>VPA</b> → adjusts CPU/memory requests of existing pods.",
]))

story.append(Q(34, "Deployment strategies in K8s"))
story.append(A("Rolling Update (default), Recreate, Blue-Green, Canary, A/B Testing."))

story.append(Q(35, "Blue-Green Deployment"))
story.append(A("Two identical environments — Blue (live) and Green (new). Switch traffic to Green after testing; instant rollback if issues."))

story.append(Q(36, "What's inside a K8s cluster?"))
story.append(A("Control plane + worker nodes running pods, plus etcd, networking (CNI), DNS (CoreDNS), and add-ons."))

story.append(Q(37, "What is etcd?"))
story.append(A("Distributed key-value store holding the entire cluster state and configuration."))

story.append(Q(38, "What is a Namespace?"))
story.append(A("Logical partition inside a cluster to isolate resources (dev/test/prod, multi-team)."))

story.append(Q(39, "kubectl describe pod"))
story.append(A("Shows events, container statuses, volumes, IPs — essential for troubleshooting."))

story.append(Q(40, "Useful kubectl commands"))
story.append(A("get pods, get svc, describe, logs, exec -it, apply -f, delete, scale, rollout status, top pod."))

story.append(Q(41, "Command to see running pods"))
story.append(Code("kubectl get pods -A"))

story.append(Q(42, "EKS vs Kubernetes"))
story.append(A("EKS is AWS-managed Kubernetes — AWS manages control plane, etcd backups, upgrades. Vanilla K8s is self-managed."))

story.append(Q(43, "Where do you store code in K8s?"))
story.append(A("Not in K8s — code lives in Git. The built image is stored in a registry (ECR/DockerHub), and K8s pulls it via manifests."))

story.append(Q(44, "How to manage multiple applications on K8s?"))
story.append(A("Use Namespaces for isolation, Helm charts for packaging, labels/selectors for grouping, and Ingress for routing."))

story.append(Q(45, "What if an error occurs during deployment?"))
story.append(A("<font face='Courier'>kubectl describe pod</font> → events, <font face='Courier'>kubectl logs &lt;pod&gt;</font> → container logs, <font face='Courier'>kubectl rollout undo deployment/&lt;name&gt;</font> to revert."))

story.append(PageBreak())

# ============ 4. JENKINS ============
story.append(Section("4. Jenkins"))

story.append(Q(46, "Jenkins Master-Slave Architecture"))
story.append(A("<b>Master</b> schedules jobs, manages config & UI. <b>Slaves (agents)</b> execute builds. Enables load distribution, parallel builds, and multi-OS environments."))

story.append(Q(47, "How to install Jenkins plugins (both ways)"))
story.extend(Bullets([
    "<b>UI:</b> Manage Jenkins → Plugins → Available → search & install.",
    "<b>Manual:</b> Download .hpi → Manage Jenkins → Plugins → Advanced → Upload Plugin.",
]))

story.append(Q(48, "How to restart Jenkins?"))
story.extend(Bullets([
    "URL: <font face='Courier'>http://&lt;jenkins&gt;/restart</font> or <font face='Courier'>/safeRestart</font>",
    "CLI: <font face='Courier'>sudo systemctl restart jenkins</font>",
]))

story.append(Q(49, "How to add tools in Jenkins?"))
story.append(A("Manage Jenkins → Tools → configure JDK, Maven, Git, Docker etc. (auto-install or path)."))

story.append(Q(50, "How to set credentials in Jenkins?"))
story.append(A("Manage Jenkins → Credentials → System → Global → Add Credentials (username/password, SSH key, secret text, AWS keys)."))

story.append(Q(51, "What is a Webhook?"))
story.append(A("HTTP callback triggered by an event (e.g., Git push). GitHub POSTs to Jenkins, triggering the pipeline."))

story.append(Q(52, "How to set up a webhook?"))
story.append(A("GitHub repo → Settings → Webhooks → Add → URL <font face='Courier'>http://&lt;jenkins&gt;/github-webhook/</font>, content type JSON. In Jenkins job, enable 'GitHub hook trigger'."))

story.append(Q(53, "What is 'Build Periodically'?"))
story.append(A("A cron-style trigger (e.g., <font face='Courier'>H/15 * * * *</font>) to run builds on a schedule."))

story.append(Q(54, "Types of Jenkins triggers"))
story.append(A("Poll SCM, Build Periodically, GitHub webhook trigger, Upstream/downstream build, Manual / parameterized."))

story.append(Q(55, "What is a Jenkinsfile?"))
story.append(A("A text file (Groovy DSL) in the repo that defines the pipeline as code (Declarative or Scripted)."))

story.append(Q(56, "Declarative Pipeline Structure"))
story.append(Code("""pipeline {
  agent any
  environment { ... }
  stages {
    stage('Build') { steps { sh 'mvn clean package' } }
    stage('Test')  { steps { sh 'mvn test' } }
    stage('Deploy'){ steps { sh '...' } }
  }
  post { always { ... } }
}"""))

story.append(Q(57, "What is an Artifact?"))
story.append(A("A build output (.jar, .war, Docker image) produced by the pipeline, stored for deployment."))

story.append(Q(58, "Plugins typically used in your project"))
story.append(A("Git, GitHub, Pipeline, Maven Integration, Docker Pipeline, Kubernetes CLI, SSH Agent, Credentials Binding, Email Extension."))

story.append(Q(59, "Post-build actions"))
story.append(A("Steps after the build — archive artifacts, email notification, trigger another job, publish reports."))

story.append(PageBreak())

# ============ 5. TERRAFORM ============
story.append(Section("5. Terraform"))

story.append(Q(60, "What is Terraform & why used?"))
story.append(A("Open-source IaC tool to provision infrastructure declaratively — reproducible, version-controlled, multi-cloud."))

story.append(Q(61, "Basic Terraform commands"))
story.append(A("init, validate, fmt, plan, apply, destroy, state, output, import, taint, refresh."))

story.append(Q(62, "Terraform stages"))
story.append(A("1) Write (.tf) → 2) Init (providers) → 3) Validate/fmt → 4) Plan → 5) Apply → 6) Destroy."))

story.append(Q(63, "terraform fmt vs terraform plan"))
story.extend(Bullets([
    "<b>fmt</b> → formats code style.",
    "<b>plan</b> → previews changes before applying.",
]))

story.append(Q(64, "terraform apply vs terraform destroy"))
story.extend(Bullets([
    "<b>apply</b> → creates/updates resources.",
    "<b>destroy</b> → removes all managed resources.",
]))

story.append(Q(65, "What is tfstate?"))
story.append(A("<font face='Courier'>terraform.tfstate</font> is the JSON file mapping config to real-world resources — Terraform's source of truth."))

story.append(Q(66, "How to check syntax in .tf file?"))
story.append(Code("terraform validate\nterraform fmt -check"))

story.append(Q(67, "Is AWS provider mandatory? What if missing?"))
story.append(A("Yes — for AWS resources you must declare the provider. Without it, <font face='Courier'>terraform init</font> fails: 'provider not found'."))

story.append(Q(68, "How to create an EC2 instance (Terraform)"))
story.append(Code("""provider "aws" { region = "ap-south-1" }

resource "aws_instance" "demo" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
  tags = { Name = "TF-EC2" }
}"""))

story.append(Q(69, "Steps to create EC2 via Terraform"))
story.append(A("1) Install Terraform & AWS CLI &nbsp; 2) Configure credentials &nbsp; 3) Write provider.tf & main.tf &nbsp; 4) terraform init &nbsp; 5) terraform plan &nbsp; 6) terraform apply."))

story.append(Q(70, "How to destroy a specific resource?"))
story.append(Code("terraform destroy -target=aws_instance.demo"))

story.append(Q(71, "Terraform Modules"))
story.append(Code("""module "vpc" {
  source = "./modules/vpc"
  cidr   = "10.0.0.0/16"
}"""))

story.append(Q(72, "CloudFormation vs Terraform"))
tbl2 = Table(
    [["CloudFormation","Terraform"],
     ["AWS-only","Multi-cloud"],
     ["JSON/YAML","HCL"],
     ["Managed by AWS","Open-source, HashiCorp"],
     ["Native AWS integration","Larger provider ecosystem"]],
    colWidths=[8*cm, 8*cm]
)
tbl2.setStyle(tbl.style if False else TableStyle([
    ("BACKGROUND",(0,0),(-1,0), colors.HexColor("#0B3D91")),
    ("TEXTCOLOR",(0,0),(-1,0), colors.white),
    ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
    ("ALIGN",(0,0),(-1,-1),"LEFT"),
    ("GRID",(0,0),(-1,-1),0.4,colors.grey),
    ("FONTSIZE",(0,0),(-1,-1),10),
    ("LEFTPADDING",(0,0),(-1,-1),6),
    ("RIGHTPADDING",(0,0),(-1,-1),6),
    ("TOPPADDING",(0,0),(-1,-1),4),
    ("BOTTOMPADDING",(0,0),(-1,-1),4),
]))
story.append(tbl2)
story.append(Spacer(1, 0.3*cm))

story.append(Q(73, "State locking (DynamoDB + S3)"))
story.append(A("S3 stores remote state; DynamoDB provides a lock so two engineers can't apply changes simultaneously."))

story.append(PageBreak())

# ============ 6. ANSIBLE ============
story.append(Section("6. Ansible"))

story.append(Q(74, "Ansible modules for configuration management"))
story.append(A("apt, yum, dnf, package, service, systemd, copy, file, template, user, group, lineinfile, command, shell, git, unarchive."))

story.append(Q(75, "Sample ansible.cfg"))
story.append(Code("""[defaults]
inventory        = ./inventory.ini
remote_user      = ubuntu
private_key_file = ~/.ssh/id_rsa
host_key_checking = False
retry_files_enabled = False"""))

story.append(Q(76, "Ansible vs Terraform"))
story.extend(Bullets([
    "<b>Terraform</b> → provisioning infrastructure (declarative).",
    "<b>Ansible</b> → configuration management on existing servers (procedural + declarative).",
]))

story.append(Q(77, "Ansible Playbook usage"))
story.append(A("YAML file defining tasks to run on hosts — installs packages, copies files, manages services, deploys apps."))

# ============ 7. GIT ============
story.append(Section("7. Git & GitHub"))

story.append(Q(78, "Basic Git commands"))
story.append(A("init, clone, add, commit, status, log, push, pull, branch, checkout, merge, rebase, revert, reset, stash."))

story.append(Q(79, "Git Push vs Pull"))
story.extend(Bullets([
    "<b>Push</b> → upload local commits to remote.",
    "<b>Pull</b> → fetch + merge remote changes into local.",
]))

story.append(Q(80, "Git Merge vs Revert"))
story.extend(Bullets([
    "<b>Merge</b> → combines two branches.",
    "<b>Revert</b> → new commit that undoes a previous commit (safe for shared branches).",
]))

story.append(Q(81, "Git Branching Strategies"))
story.append(A("Git Flow (main, develop, feature, release, hotfix), GitHub Flow (main + short-lived branches), Trunk-Based Development, Forking workflow."))

story.append(Q(82, "Trunk-Based Development"))
story.append(A("All developers commit small frequent changes to a shared trunk (main). Feature flags hide incomplete work. Enables continuous integration."))

story.append(Q(83, "What is a Hotfix?"))
story.append(A("Urgent fix branched from main/production to patch a critical bug, merged back to both main and develop."))

story.append(Q(84, "Command to create a new branch"))
story.append(Code("git checkout -b feature/login"))

story.append(Q(85, "Command to see a specific commit"))
story.append(Code("git show <commit-hash>"))

story.append(Q(86, "Git vs GitHub"))
story.append(A("<b>Git</b> → distributed VCS (local tool). <b>GitHub</b> → cloud hosting platform with collaboration features."))

story.append(Q(87, "Steps to change a branch in a repo"))
story.append(Code("""git clone <repo>
git checkout -b feature
# edit files
git add . && git commit -m "msg"
git push origin feature
# open PR on GitHub"""))

story.append(PageBreak())

# ============ 8. AWS ============
story.append(Section("8. AWS"))

story.append(Q(88, "IaaS, PaaS, SaaS examples"))
story.extend(Bullets([
    "<b>IaaS</b> → EC2, VPC, EBS",
    "<b>PaaS</b> → Elastic Beanstalk, RDS, Lambda",
    "<b>SaaS</b> → Amazon WorkMail, Chime, QuickSight",
]))

story.append(Q(89, "EC2 — IaaS or PaaS?"))
story.append(A("<b>IaaS</b> — you manage OS, runtime, and apps; AWS provides only the VM."))

story.append(Q(90, "What is VPC?"))
story.append(A("Virtual Private Cloud — logically isolated network in AWS. You control IP range, subnets, route tables, gateways."))

story.append(Q(91, "Public vs Private Subnet"))
story.extend(Bullets([
    "<b>Public</b> → routes to Internet Gateway; resources can have public IPs.",
    "<b>Private</b> → no direct internet; access via NAT Gateway.",
]))

story.append(Q(92, "Can we create EC2 without VPC?"))
story.append(A("No — every EC2 must be inside a VPC. AWS provides a default VPC if none exists."))

story.append(Q(93, "How to connect to an EC2 from a terminal?"))
story.append(Code("ssh -i key.pem ec2-user@<public-ip>"))

story.append(Q(94, "S3 — full form & scope"))
story.append(A("<b>Simple Storage Service.</b> Global service (console), but buckets are region-specific. Bucket names are globally unique."))

story.append(Q(95, "S3 Storage Classes"))
story.append(A("Standard, Standard-IA, One Zone-IA, Intelligent-Tiering, Glacier Instant Retrieval, Glacier Flexible Retrieval, Glacier Deep Archive."))

story.append(Q(96, "What is AWS Lambda?"))
story.append(A("Serverless compute — runs code in response to events. No server management; pay per execution."))

story.append(Q(97, "Scaling & Security in AWS"))
story.extend(Bullets([
    "<b>Scaling</b> → Auto Scaling Groups, ELB, HPA on EKS.",
    "<b>Security</b> → IAM, Security Groups, NACLs, KMS, WAF, GuardDuty.",
]))

story.append(Q(98, "Migrating an on-prem 2-tier app to AWS"))
story.append(A("Assess (Migration Hub) → Setup VPC + subnets → Deploy frontend (EC2/ECS behind ALB) → Deploy backend (EC2/RDS) → Route 53 + CloudFront → DMS for data → Test & cutover."))

story.append(Q(99, "What is Latency?"))
story.append(A("Time delay between request and response — measured in ms. Reduced via CDN, caching, region proximity."))

story.append(PageBreak())

# ============ 9. CI/CD GENERAL ============
story.append(Section("9. CI/CD & General"))

story.append(Q(100, "What is CI/CD?"))
story.append(A("<b>Continuous Integration</b> → frequently merging code with automated builds/tests. <b>Continuous Delivery/Deployment</b> → automated release to staging/production."))

story.append(Q(101, "Project Workflow (sample answer)"))
story.append(A("<i>Developer pushes code to GitHub → webhook triggers Jenkins (master-slave) → Maven builds the WAR → Docker image created → pushed to AWS ECR → Ansible/kubectl deploys to EKS → service exposed via LoadBalancer/Ingress → monitoring via CloudWatch.</i>"))

story.append(Q(102, "Why Declarative Pipeline?"))
story.append(A("Simpler, structured syntax; easier to maintain; built-in error handling; better for teams."))

story.append(Q(103, "What is Maven?"))
story.append(A("A build & dependency management tool for Java projects using pom.xml."))

story.append(Q(104, "What is Tomcat?"))
story.append(A("Open-source Java servlet container that runs WAR files."))

story.append(Q(105, "Can Tomcat be used in production?"))
story.append(A("Yes, but typically behind a reverse proxy (Nginx/Apache/ALB) with hardening, HTTPS, and clustering for HA."))

story.append(Q(106, "How to know if an application is secure?"))
story.extend(Bullets([
    "Static code analysis (SonarQube)",
    "Dependency scans (Snyk, OWASP)",
    "HTTPS everywhere",
    "Authentication/Authorization checks",
    "Penetration testing",
    "Vulnerability scans on container images (Trivy)",
]))

story.append(Q(107, "What is CrashLoopBackOff?"))
story.append(A("K8s state where a pod keeps crashing & restarting. Causes: bad image, missing config, failed liveness probe, app exception. Diagnose with <font face='Courier'>kubectl logs</font> & <font face='Courier'>describe</font>."))

story.append(Q(108, "Troubleshooting commands toolkit"))
story.append(A("ping, curl, netstat, ss, top, df -h, journalctl -u, tail -f /var/log/..., systemctl status, kubectl describe/logs, docker logs."))

story.append(Q(109, "Have you used AI to troubleshoot errors? (sample)"))
story.append(A("<i>Yes — I use Copilot/ChatGPT to quickly decode unfamiliar errors, suggest fixes, and explain stack traces, but I always verify by reading official docs and testing in a sandbox before applying.</i>"))

story.append(Q(110, "Any questions for the interviewer? (always ask!)"))
story.extend(Bullets([
    "What does success look like in this role in the first 6 months?",
    "What tools and cloud platforms does the team primarily use?",
    "How is on-call/incident management structured?",
    "What learning/upskilling opportunities are available?",
]))

story.append(Spacer(1, 1*cm))
story.append(P("— End of Document —",
               ParagraphStyle("end", parent=answer_style, alignment=TA_CENTER,
                              fontName="Helvetica-Oblique", textColor=colors.grey)))

# ------------ Build PDF ------------
doc = SimpleDocTemplate(
    out_path, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
    title="DevOps Interview Q&A",
    author="Prepared for Dhame Pratik Sanjay"
)

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.grey)
    canvas.drawRightString(A4[0]-2*cm, 1.2*cm, f"Page {doc.page}")
    canvas.drawString(2*cm, 1.2*cm, "DevOps Interview Q&A")
    canvas.restoreState()

doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

size_kb = os.path.getsize(out_path)/1024
print(f"PDF created: {out_path}")
print(f"File size  : {size_kb:.1f} KB")

