import sys
import re

def create_contact_page():
    with open('faculty.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    header_split = content.split('<div class="page-content">')
    header = header_split[0] + '<div class="page-content">\n'
    
    footer_split = content.split('<!-- Footer -->')
    footer = '      <!-- Footer -->' + footer_split[1]
    
    # Let's fix the title in the header
    header = re.sub(r'<title>.*?</title>', '<title>Contact Us | IIITP Pune</title>', header)
    
    # Add our custom styles just before </head>
    custom_styles = """
    <style>
        .contact-header { text-align: center; margin-bottom: 40px; margin-top: 20px; }
        .contact-header h1 { color: #174873; font-weight: 700; margin-bottom: 10px; }
        .contact-header p { font-size: 1.1rem; color: #555; }
        
        .contact-top-row { display: flex; flex-wrap: wrap; gap: 30px; justify-content: center; margin-bottom: 50px; }
        .info-card { flex: 1; min-width: 300px; max-width: 450px; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 4px solid #174873; }
        .info-card h3 { color: #e85d04; margin-bottom: 15px; font-size: 1.3rem; }
        .info-card p { margin-bottom: 10px; color: #444; line-height: 1.6; }
        .info-card i { color: #174873; margin-right: 10px; width: 20px; text-align: center; }
        
        .reach-section { background: #f4f6fb; padding: 40px; border-radius: 8px; margin-bottom: 50px; }
        .reach-section h2 { text-align: center; color: #174873; margin-bottom: 30px; }
        .reach-grid { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }
        .reach-item { background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); width: 220px; text-align: center; transition: transform 0.3s; }
        .reach-item:hover { transform: translateY(-5px); }
        .reach-item i { font-size: 2rem; color: #e85d04; margin-bottom: 15px; }
        .reach-item h4 { color: #174873; margin-bottom: 10px; }
        .reach-item p { color: #666; font-size: 0.9rem; margin-bottom: 15px; }
        .reach-item a { display: inline-block; padding: 6px 12px; background: #174873; color: #fff; border-radius: 4px; text-decoration: none; font-size: 0.85rem; transition: background 0.3s; }
        .reach-item a:hover { background: #e85d04; }

        .contacts-section h2 { text-align: center; color: #174873; margin-bottom: 30px; }
        .contacts-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .contact-card { background: #fff; border: 1px solid #eaeaea; padding: 25px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); transition: transform 0.3s, box-shadow 0.3s; border-left: 4px solid #174873; display: flex; flex-direction: column; }
        .contact-card:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(232, 93, 4, 0.12); border-left-color: #e85d04; }
        .contact-card h4 { color: #174873; font-size: 1.1rem; margin-bottom: 5px; }
        .contact-card .role { color: #e85d04; font-size: 0.9rem; font-weight: 600; margin-bottom: 15px; }
        .contact-card p { font-size: 0.95rem; color: #555; margin-bottom: 8px; display: flex; align-items: flex-start; }
        .contact-card p i { margin-top: 4px; margin-right: 10px; color: #888; }
        .contact-card a { color: #174873; text-decoration: none; }
        .contact-card a:hover { color: #e85d04; }
        .contact-card .card-content { flex: 1; }
    </style>
</head>"""
    header = header.replace('</head>', custom_styles)
    
    # Build custom content
    contact_html = """
    <div class="contact-header">
        <h1><strong>Contact Us</strong></h1>
        <p>Get in touch with the Indian Institute of Information Technology, Pune</p>
    </div>

    <div class="contact-top-row">
        <div class="info-card">
            <h3><i class="fas fa-map-marker-alt"></i> Campus Location</h3>
            <p>Indian Institute of Information Technology, Pune</p>
            <p>Gat No - 5 & 6,<br>
            Vill - Nanoli-Tarf Chakan, PO - Talegaon,<br>
            Tah - Maval, Dist-Pune,<br>
            Maharashtra-410507</p>
        </div>
        <div class="info-card">
            <h3><i class="fas fa-info-circle"></i> General Enquiry</h3>
            <p><i class="far fa-clock"></i> Monday - Saturday: 10:00 AM – 5:00 PM</p>
            <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224510" style="color: inherit; text-decoration: none;">02114-224510</a></p>
            <p><i class="fas fa-envelope"></i> <a href="mailto:enquiry@iiitp.ac.in" style="color: inherit; text-decoration: none;">enquiry@iiitp.ac.in</a></p>
        </div>
    </div>

    <div class="reach-section">
        <h2>How to Reach IIIT Pune</h2>
        <div class="reach-grid">
            <div class="reach-item">
                <i class="fas fa-train"></i>
                <h4>Railway</h4>
                <p>Talegaon Railway Station<br>Distance: 6.2 km</p>
                <a href="https://www.google.com/maps/dir/Talegaon+Railway+Station,+Talegaon+Dabhade,+Maharashtra/IIIT+Pune+Main+Rd,+Akurdi,+Maharashtra+410507/@18.7479179,73.6501962,14z/" target="_blank">View on Map</a>
            </div>
            <div class="reach-item">
                <i class="fas fa-bus"></i>
                <h4>Bus</h4>
                <p>Talegaon Bus Stand<br>Distance: 5.9 km</p>
                <a href="https://www.google.com/maps/dir/Talegaon+Dabhade,+Maharashtra/IIIT+Pune+Main+Rd,+Akurdi,+Maharashtra/@18.762252,73.6867981,16.54z/" target="_blank">View on Map</a>
            </div>
            <div class="reach-item">
                <i class="fas fa-plane"></i>
                <h4>Air</h4>
                <p>Pune Airport<br>Distance: 43.2 km</p>
                <a href="https://www.google.com/maps/dir/Pune+International+Airport,+New+Airport+Rd,+Pune+International+Airport+Area,+Lohegaon,+Pune,+Maharashtra+411032/IIIT+Pune+Main+Rd,+Akurdi,+Maharashtra+410507/@18.6658708,73.6944074,12z/" target="_blank">View on Map</a>
            </div>
            <div class="reach-item">
                <i class="fas fa-car"></i>
                <h4>Road</h4>
                <p>L&T Circle<br>Distance: 2.2 km</p>
                <a href="https://www.google.com/maps/dir/L%26T+Circle,+Maharashtra+410507/IIIT+Pune+Main+Rd,+Akurdi,+Maharashtra+410507/@18.7655455,73.6844449,16z/" target="_blank">View on Map</a>
            </div>
        </div>
    </div>

    <div class="contacts-section">
        <h2>Key Contacts</h2>
        <div class="contacts-grid">
            <!-- Contact Card 1 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Director's PA</h4>
                    <div class="role">Administration</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224501">02114-224501</a></p>
                </div>
            </div>
            <!-- Contact Card 2 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Viraj Pradip Lohakare</h4>
                    <div class="role">Registrar's PA</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224503">02114-224503</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:patoreg@iiitp.ac.in">patoreg@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 3 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Mr. Kedar Bhogshetti</h4>
                    <div class="role">Training & Placements Officer</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224508">02114-224508</a>, <a href="tel:+919326479440">+91 9326479440</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:placements@iiitp.ac.in">placements@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 4 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Kaptan Singh</h4>
                    <div class="role">Faculty I/C Training & Placement</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+919826524212">+91 9826524212</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:kaptansingh@iiitp.ac.in">kaptansingh@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 5 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Sanjeev Sharma</h4>
                    <div class="role">Associate Dean (Academics) / CVO</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224504">02114-224504</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:sanjeevsharma@iiitp.ac.in">sanjeevsharma@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 6 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Sushant Kumar</h4>
                    <div class="role">Associate Dean (R&D and Faculty Welfare)</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+918292305145">+91 8292305145</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:sushant@iiitp.ac.in">sushant@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 7 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Bhupendra Singh</h4>
                    <div class="role">HoD (CSE) / Admission / Associate Dean</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224505">02114-224505</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:bhupendra@iiitp.ac.in">bhupendra@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 8 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Nagendra Kushwaha</h4>
                    <div class="role">HoD (ECE)</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224506">02114-224506</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:nagendra@iiitp.ac.in">nagendra@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 9 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Jatin Majithia</h4>
                    <div class="role">HoD (AS&H)</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224507">02114-224507</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:jatinmajithia@iiitp.ac.in">jatinmajithia@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 10 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Girl's Hostel (GH Office)</h4>
                    <div class="role">Hostel Administration</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224511">02114-224511</a></p>
                </div>
            </div>
            <!-- Contact Card 11 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Boy's Hostel 01 (BH1 Office)</h4>
                    <div class="role">Hostel Administration</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224512">02114-224512</a></p>
                </div>
            </div>
            <!-- Contact Card 12 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Boy's Hostel 02 (BH2 Office)</h4>
                    <div class="role">Hostel Administration</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224513">02114-224513</a></p>
                </div>
            </div>
            <!-- Contact Card 13 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Shubham Shukla</h4>
                    <div class="role">Chief Warden</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+919532523961">+91 9532523961</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:shubhamshukla@iiitp.ac.in">shubhamshukla@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 14 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Dheeraj Dubey</h4>
                    <div class="role">Boy's Hostel 1 Warden</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+918840677530">+91 8840677530</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:dheeraj@iiitp.ac.in">dheeraj@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 15 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Mahesh Joshi</h4>
                    <div class="role">Co-ordinator (PG/Ph.D.) / Boys' Hostel 2 Warden</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+918886844737">+91 8886844737</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:mahesh.joshi@iiitp.ac.in">mahesh.joshi@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 16 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Dr. Habila Basumatary</h4>
                    <div class="role">Warden (Girls)</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+918133911040">+91 8133911040</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:habila@iiitp.ac.in">habila@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 17 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Mr. Laxman Shinde</h4>
                    <div class="role">Jr. Superintendent (Boys/Girls)</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+919881729759">+91 9881729759</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:laxmanshinde@iiitp.ac.in">laxmanshinde@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 18 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Mr. Aman Ankur</h4>
                    <div class="role">Purchase Section</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:02114-224509">02114-224509</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:js1.procurement@iiitp.ac.in">js1.procurement@iiitp.ac.in</a></p>
                </div>
            </div>
            <!-- Contact Card 19 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Shri Lalit Chandra Trivedi</h4>
                    <div class="role">Independent External Monitor (Purchase)</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+919967567679">+91 9967567679</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:lctrivedi61@gmail.com">lctrivedi61@gmail.com</a></p>
                </div>
            </div>
            <!-- Contact Card 20 -->
            <div class="contact-card">
                <div class="card-content">
                    <h4>Ashok Kumar Tripathy, IAS (Retd.)</h4>
                    <div class="role">Independent External Monitor (Purchase)</div>
                    <p><i class="fas fa-phone-alt"></i> <a href="tel:+919437040285">+91 9437040285</a></p>
                    <p><i class="fas fa-envelope"></i> <a href="mailto:tripathyak@yahoo.com">tripathyak@yahoo.com</a></p>
                </div>
            </div>
        </div>
    </div>
    </div> <!-- Closes .page-content -->
"""

    # We also need to fix the script in the footer (remove the filter script)
    footer = re.sub(r'<script>.*?</script>', '', footer, flags=re.DOTALL)
    
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(header + contact_html + footer)

if __name__ == '__main__':
    create_contact_page()
