<div align="center">

<h3><code>ashish@github ~ $ ./contributions.sh</code></h3>
<img src="./contrib-heatmap.svg" width="860" />

<br><br>

<h3><code>ashish@github ~ $ whoami</code></h3>
<table>
  <tr>
    <td valign="top"><img src="./profile-ascii.svg" width="370" /></td>
    <td valign="top"><img src="./info-card.svg" width="490" /></td>
  </tr>
</table>

<br><br>

<h3><code>ashish@github ~ $ ./links.sh</code></h3>

**Full Stack Developer · Freelancer · React & Next.js**

[![Portfolio](https://img.shields.io/badge/Portfolio-ashishupadhyay.me-0d1117?style=for-the-badge&logo=vercel&logoColor=white)](https://ashishupadhyay.me/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ashish_Kumar_Upadhyay-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashish-kumar-upadhyay-071499284)
[![Gmail](https://img.shields.io/badge/Gmail-ashishkumarupadhyay0328@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ashishkumarupadhyay0328@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Ashish--kumar--upadhyay-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ashish-kumar-upadhyay)

</div>

---

### Featured projects

| Project | Stack | Link |
| --- | --- | --- |
| Dubai Perfume E-Commerce | Next.js · MongoDB · Vercel | [noamani.com](https://www.noamani.com/) |
| LMS Platform | React · Firebase | [learnxplatform.qzz.io](https://learnxplatform.qzz.io/) |
| Kitchen Recipe App | React · Firebase · Vite | [Live](https://recpie-kitchen.vercel.app/) · [GitHub](https://github.com/Ashish-kumar-upadhyay/recpie-kitchen) |

---

<details>
<summary><code>ashish@github ~ $ cat README.md --regenerate</code></summary>

Portrait and info card (when you change photo or bio):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r scripts/requirements.txt
python scripts/prep_photo.py assets/profile.png source-prepped.png
python scripts/make_ascii_svg.py source-prepped.png profile-ascii.svg
python scripts/make_info_card.py
```

Contribution heatmap (also runs daily via GitHub Actions):

```bash
pip install requests beautifulsoup4
python scripts/fetch_contributions.py
python scripts/render_heatmap_svg.py
```

</details>
