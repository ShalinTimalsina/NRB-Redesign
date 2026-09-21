from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path('pages/publications/know-your-bank-notes/index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# New gorgeous UI for Bank Notes
ui_html = """
<div class="nrb-section-shell py-14">
    <!-- Intro text -->
    <div class="max-w-3xl mb-12">
        <h2 class="text-3xl font-bold text-[#25295B] mb-4">Security Features of Nepali Banknotes</h2>
        <p class="text-slate-600 text-lg leading-relaxed">
            Nepal Rastra Bank incorporates advanced security features into its banknotes to prevent counterfeiting and ensure public trust. Learn how to verify the authenticity of your banknotes using the <strong>Look, Feel, and Tilt</strong> method.
        </p>
    </div>

    <!-- Rs 1000 Note Section -->
    <div class="mb-20">
        <div class="flex items-center gap-4 mb-8">
            <div class="h-10 w-2 bg-[#138496] rounded-full"></div>
            <h3 class="text-3xl font-bold text-slate-900 tracking-tight">Rs. 1000</h3>
        </div>

        <div class="grid lg:grid-cols-2 gap-10 mb-12">
            <!-- Front Image -->
            <div class="bg-white p-6 rounded-[14px] shadow-sm border border-slate-200">
                <h4 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-400 mb-4">Obverse (Front)</h4>
                <div class="rounded-xl overflow-hidden bg-slate-50 flex items-center justify-center p-4">
                    <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_note_front_img-1.png" alt="Rs. 1000 Front" class="w-full object-contain drop-shadow-lg hover:scale-[1.02] transition-transform duration-300">
                </div>
            </div>
            <!-- Back Image -->
            <div class="bg-white p-6 rounded-[14px] shadow-sm border border-slate-200">
                <h4 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-400 mb-4">Reverse (Back)</h4>
                <div class="rounded-xl overflow-hidden bg-slate-50 flex items-center justify-center p-4">
                    <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_note_back_img-1.png" alt="Rs. 1000 Back" class="w-full object-contain drop-shadow-lg hover:scale-[1.02] transition-transform duration-300">
                </div>
            </div>
        </div>

        <!-- Security Features Grid -->
        <h4 class="text-xl font-bold text-[#25295B] mb-6">Security Features Guide</h4>
        <div class="grid md:grid-cols-3 gap-6">
            
            <!-- LOOK -->
            <div class="bg-white rounded-[14px] p-8 border border-slate-200 shadow-sm relative overflow-hidden group hover:border-[#138496]/50 transition-colors nrb-elevated-card">
                <div class="absolute top-0 right-0 w-24 h-24 bg-[#138496]/5 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                <div class="flex items-center gap-3 mb-6 relative z-10">
                    <div class="w-10 h-10 rounded-full bg-[#138496]/10 text-[#138496] flex items-center justify-center">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                    </div>
                    <h5 class="text-lg font-bold text-slate-900">Look</h5>
                </div>
                <ul class="space-y-6 relative z-10">
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_1.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Watermark">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Watermark</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Hold the banknote against the light to clearly see the rhododendron watermark.</p>
                        </div>
                    </li>
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_2.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Register">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">See Through Register</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Hold up to the light to see the number "1000" fit perfectly together.</p>
                        </div>
                    </li>
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_3.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Thread">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Security Thread</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Visible letters "NRB" and number "1000" in the thread.</p>
                        </div>
                    </li>
                </ul>
            </div>

            <!-- FEEL -->
            <div class="bg-white rounded-[14px] p-8 border border-slate-200 shadow-sm relative overflow-hidden group hover:border-[#25295B]/50 transition-colors nrb-elevated-card">
                <div class="absolute top-0 right-0 w-24 h-24 bg-[#25295B]/5 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                <div class="flex items-center gap-3 mb-6 relative z-10">
                    <div class="w-10 h-10 rounded-full bg-[#25295B]/10 text-[#25295B] flex items-center justify-center">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 11.5V14m0-2.5v-6a1.5 1.5 0 113 0m-3 6a1.5 1.5 0 00-3 0v2a7.5 7.5 0 0015 0v-5a1.5 1.5 0 00-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 013 0v1m0 0V11m0-5.5a1.5 1.5 0 013 0v3m0 0V11"></path></svg>
                    </div>
                    <h5 class="text-lg font-bold text-slate-900">Feel</h5>
                </div>
                <ul class="space-y-6 relative z-10">
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_4.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Raised Inks">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Raised Inks</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Run fingers over the note to feel thicker ink areas.</p>
                        </div>
                    </li>
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_5.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Braille">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Braille Feature</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Touch the raised "M" with your fingers (for the visually impaired).</p>
                        </div>
                    </li>
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_6.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Emboss">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Emboss</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Feel the distinctly raised surface textures.</p>
                        </div>
                    </li>
                </ul>
            </div>

            <!-- TILT -->
            <div class="bg-white rounded-[14px] p-8 border border-slate-200 shadow-sm relative overflow-hidden group hover:border-[#16A34A]/50 transition-colors nrb-elevated-card">
                <div class="absolute top-0 right-0 w-24 h-24 bg-[#16A34A]/5 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
                <div class="flex items-center gap-3 mb-6 relative z-10">
                    <div class="w-10 h-10 rounded-full bg-[#16A34A]/10 text-[#16A34A] flex items-center justify-center">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                    </div>
                    <h5 class="text-lg font-bold text-slate-900">Tilt</h5>
                </div>
                <ul class="space-y-6 relative z-10">
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_7.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Thread Tilt">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Dynamic Thread</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">The thread shows a dynamic color-shifting effect when tilted.</p>
                        </div>
                    </li>
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_8.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Metallic">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Metallic Silver</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">Embossed areas reveal a metallic silver sheen on tilt.</p>
                        </div>
                    </li>
                    <li class="flex gap-4">
                        <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_9.png" class="w-12 h-12 rounded bg-slate-50 object-cover shadow-sm border border-slate-100" alt="Iridescent">
                        <div>
                            <p class="font-semibold text-sm text-slate-900">Iridescent Ink</p>
                            <p class="text-xs text-slate-500 mt-1 leading-relaxed">An obvious iridescent glow appears in specific painted zones.</p>
                        </div>
                    </li>
                </ul>
            </div>

        </div>
    </div>
    
    <!-- More Notes Placeholder / Mini Cards -->
    <div class="pt-10 border-t border-slate-200">
        <h4 class="text-lg font-bold text-slate-900 mb-6">Explore Other Denominations</h4>
        <div class="flex gap-4 overflow-x-auto pb-4">
            <a href="#" class="flex items-center justify-between bg-white border border-slate-200 rounded-xl px-5 py-4 w-64 hover:border-[#138496] transition-colors group shadow-sm shrink-0">
                <span class="font-bold text-slate-700 group-hover:text-[#138496]">Rs. 500</span>
                <svg class="w-4 h-4 text-slate-400 group-hover:text-[#138496] transform group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </a>
            <a href="#" class="flex items-center justify-between bg-white border border-slate-200 rounded-xl px-5 py-4 w-64 hover:border-[#138496] transition-colors group shadow-sm shrink-0">
                <span class="font-bold text-slate-700 group-hover:text-[#138496]">Rs. 100</span>
                <svg class="w-4 h-4 text-slate-400 group-hover:text-[#138496] transform group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </a>
            <a href="#" class="flex items-center justify-between bg-white border border-slate-200 rounded-xl px-5 py-4 w-64 hover:border-[#138496] transition-colors group shadow-sm shrink-0">
                <span class="font-bold text-slate-700 group-hover:text-[#138496]">Rs. 50</span>
                <svg class="w-4 h-4 text-slate-400 group-hover:text-[#138496] transform group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </a>
        </div>
    </div>
</div>
"""

bank_notes_section = soup.find('section', id='bank-notes-content')
if bank_notes_section:
    new_section = BeautifulSoup(f'<section class="bg-[#F8FAFC]" id="bank-notes-content">{ui_html}</section>', 'html.parser')
    bank_notes_section.replace_with(new_section)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Re-designed Know Your Bank Notes page successfully.")
else:
    print("Could not find the section.")
