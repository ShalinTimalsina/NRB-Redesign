import os
import re

# 1. Update Economic Review
economic_review_html_path = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/publications/economic-review/index.html'

economic_review_content = """
<section class="py-14 border-b border-slate-200 bg-slate-50" id="documents">
    <div class="nrb-section-shell">
        <div class="flex items-center justify-between mb-8">
            <div>
                <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500">Economic Review Archive</h3>
                <p class="text-sm text-slate-600 mt-1">Official economic review publications from 2020 onwards.</p>
            </div>
            <a href="https://www.nrb.org.np/contents/uploads/2026/05/Standard-Operating-Procedure-for-NRB-Economic-Review-and-Working-Paper-1.pdf" target="_blank" class="text-sm font-medium text-[#138496] hover:text-[#25295B] flex items-center gap-2 transition-colors">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                Guidelines for Article Submission
            </a>
        </div>

        <div class="space-y-10">
            <!-- 2026 -->
            <div>
                <h4 class="text-lg font-bold text-slate-900 mb-4 pb-2 border-b border-slate-200">2026</h4>
                <div class="flex flex-col gap-3">
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/year-2026-volume-37-no-1/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - Volume 37, No. 1</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2026</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                </div>
            </div>

            <!-- 2025 -->
            <div>
                <h4 class="text-lg font-bold text-slate-900 mb-4 pb-2 border-b border-slate-200">2025</h4>
                <div class="flex flex-col gap-3">
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/year-2025-volume-35_12/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - Volume 35, 12</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2025</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                </div>
            </div>

            <!-- 2023 -->
            <div>
                <h4 class="text-lg font-bold text-slate-900 mb-4 pb-2 border-b border-slate-200">2023</h4>
                <div class="flex flex-col gap-3">
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/year-2023-volume-34_12/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - Volume 34, 12</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2023</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                </div>
            </div>

            <!-- 2022 -->
            <div>
                <h4 class="text-lg font-bold text-slate-900 mb-4 pb-2 border-b border-slate-200">2022</h4>
                <div class="flex flex-col gap-3">
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/year-2022-volume-34_2/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - Volume 34, 2</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2022</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/2022/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - 2022</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2022</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                </div>
            </div>

            <!-- 2021 -->
            <div>
                <h4 class="text-lg font-bold text-slate-900 mb-4 pb-2 border-b border-slate-200">2021</h4>
                <div class="flex flex-col gap-3">
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/year-2021-volume-33_12/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - Volume 33, 12</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2021</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                </div>
            </div>

            <!-- 2020 -->
            <div>
                <h4 class="text-lg font-bold text-slate-900 mb-4 pb-2 border-b border-slate-200">2020</h4>
                <div class="flex flex-col gap-3">
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/year-2020-volume-32-2/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - Volume 32, 2</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2020</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                    <a class="hub-card nrb-elevated-card flex items-center justify-between p-5 bg-white border border-slate-200 rounded-[14px] hover:border-[#138496] group transition-colors" href="https://www.nrb.org.np/economic-review/year-2020-volume-32-1/" target="_blank">
                        <div class="flex items-start gap-4">
                            <div class="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-[#25295B] group-hover:bg-[#138496]/10 group-hover:text-[#138496] transition-colors mt-0.5">
                                <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" x2="8" y1="13" y2="13"></line><line x1="16" x2="8" y1="17" y2="17"></line></svg>
                            </div>
                            <div class="flex flex-col gap-1.5">
                                <p class="font-semibold text-base text-slate-900 group-hover:text-[#138496] transition-colors leading-snug">Economic Review - Volume 32, 1</p>
                                <div class="flex items-center text-[13px] text-slate-500"><span class="font-medium text-slate-700">WEB</span><span class="text-slate-300 px-1.5">•</span><span>2020</span></div>
                            </div>
                        </div>
                        <div class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-slate-50 text-slate-400 group-hover:bg-[#138496] group-hover:text-white transition-colors ml-4"><svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>
"""

with open(economic_review_html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the dummy document grid with the real one
html_content = re.sub(r'<section class="py-14 border-b border-slate-200 bg-slate-50" id="documents">.*?</section>', economic_review_content, html_content, flags=re.DOTALL)

with open(economic_review_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated Economic Review.")

# 2. Update Know Your Bank Notes
notes_html_path = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/publications/know-your-bank-notes/index.html'

notes_content = """
<section class="py-14 bg-white border-b border-slate-200">
    <div class="nrb-section-shell">
        <header class="mb-10 text-center max-w-3xl mx-auto">
            <h2 class="text-3xl font-bold text-slate-900">Security Features of Nepali Banknotes</h2>
            <p class="mt-3 text-slate-600">Learn how to authenticate Rs. 1000 and Rs. 500 notes by looking for watermarks, feeling raised ink, and tilting to see security threads.</p>
        </header>

        <div class="space-y-16">
            <!-- Rs 1000 -->
            <div class="bg-slate-50 rounded-[24px] border border-slate-200 p-8 lg:p-12">
                <div class="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
                    <h3 class="text-2xl font-bold text-[#25295B]">Rs. 1000 Banknote</h3>
                    <span class="bg-[#25295B]/10 text-[#25295B] px-3 py-1 rounded-full text-sm font-semibold uppercase tracking-wider">Features</span>
                </div>
                
                <div class="grid lg:grid-cols-2 gap-12">
                    <div class="space-y-8">
                        <div>
                            <h4 class="text-sm font-semibold uppercase tracking-wider text-slate-500 mb-4">Obverse (Front)</h4>
                            <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_note_front_img-1.png" alt="Rs 1000 Note Front" class="w-full rounded-xl shadow-sm border border-slate-200">
                        </div>
                        <div>
                            <h4 class="text-sm font-semibold uppercase tracking-wider text-slate-500 mb-4">Reverse (Back)</h4>
                            <img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_note_back_img-1.png" alt="Rs 1000 Note Back" class="w-full rounded-xl shadow-sm border border-slate-200">
                        </div>
                    </div>
                    
                    <div class="space-y-10">
                        <div>
                            <h4 class="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
                                <svg class="w-5 h-5 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                Look
                            </h4>
                            <ul class="space-y-6">
                                <li class="flex gap-4 items-start">
                                    <div class="w-16 h-16 shrink-0 rounded-lg overflow-hidden border border-slate-200 bg-white"><img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_1.png" class="w-full h-full object-cover"></div>
                                    <div>
                                        <p class="font-semibold text-slate-900 text-sm">Watermark</p>
                                        <p class="text-sm text-slate-600 mt-1">Hold the banknote up to the light to clearly see the rhododendron shape.</p>
                                    </div>
                                </li>
                                <li class="flex gap-4 items-start">
                                    <div class="w-16 h-16 shrink-0 rounded-lg overflow-hidden border border-slate-200 bg-white"><img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_2.png" class="w-full h-full object-cover"></div>
                                    <div>
                                        <p class="font-semibold text-slate-900 text-sm">See Through Register</p>
                                        <p class="text-sm text-slate-600 mt-1">Hold to the light, you can see the number "1000". The image should be very clear.</p>
                                    </div>
                                </li>
                                <li class="flex gap-4 items-start">
                                    <div class="w-16 h-16 shrink-0 rounded-lg overflow-hidden border border-slate-200 bg-white"><img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_3.png" class="w-full h-full object-cover"></div>
                                    <div>
                                        <p class="font-semibold text-slate-900 text-sm">Security Thread</p>
                                        <p class="text-sm text-slate-600 mt-1">When you tilt, you can see the letters "NRB" and the number "1000".</p>
                                    </div>
                                </li>
                            </ul>
                        </div>
                        
                        <div>
                            <h4 class="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
                                <svg class="w-5 h-5 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 11.5V14m0-2.5v-6a1.5 1.5 0 113 0m-3 6a1.5 1.5 0 00-3 0v2a7.5 7.5 0 0015 0v-5a1.5 1.5 0 00-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 013 0v1m0 0V11m0-5.5a1.5 1.5 0 013 0v3m0 0V11"></path></svg>
                                Feel
                            </h4>
                            <ul class="space-y-6">
                                <li class="flex gap-4 items-start">
                                    <div class="w-16 h-16 shrink-0 rounded-lg overflow-hidden border border-slate-200 bg-white"><img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_4.png" class="w-full h-full object-cover"></div>
                                    <div>
                                        <p class="font-semibold text-slate-900 text-sm">Raised Inks</p>
                                        <p class="text-sm text-slate-600 mt-1">Run your fingers over the banknote and feel the areas where the ink is thicker.</p>
                                    </div>
                                </li>
                                <li class="flex gap-4 items-start">
                                    <div class="w-16 h-16 shrink-0 rounded-lg overflow-hidden border border-slate-200 bg-white"><img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_5.png" class="w-full h-full object-cover"></div>
                                    <div>
                                        <p class="font-semibold text-slate-900 text-sm">Braille</p>
                                        <p class="text-sm text-slate-600 mt-1">Feature for the Impaired. Touch the raised "M" with your fingers.</p>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Rs 500 -->
            <div class="bg-slate-50 rounded-[24px] border border-slate-200 p-8 lg:p-12">
                <div class="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
                    <h3 class="text-2xl font-bold text-[#25295B]">Rs. 500 Banknote</h3>
                    <span class="bg-[#25295B]/10 text-[#25295B] px-3 py-1 rounded-full text-sm font-semibold uppercase tracking-wider">Features</span>
                </div>
                
                <div class="grid lg:grid-cols-2 gap-12">
                    <div class="space-y-8">
                        <div>
                            <h4 class="text-sm font-semibold uppercase tracking-wider text-slate-500 mb-4">Obverse (Front)</h4>
                            <img src="https://www.nrb.org.np/contents/uploads/2026/07/500_note_front_img.png" alt="Rs 500 Note Front" class="w-full rounded-xl shadow-sm border border-slate-200">
                        </div>
                    </div>
                    
                    <div class="space-y-10">
                        <div>
                            <h4 class="text-xl font-bold text-slate-900 mb-4 flex items-center gap-2">
                                <svg class="w-5 h-5 text-[#138496]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"></path></svg>
                                Tilt
                            </h4>
                            <ul class="space-y-6">
                                <li class="flex gap-4 items-start">
                                    <div class="w-16 h-16 shrink-0 rounded-lg overflow-hidden border border-slate-200 bg-white"><img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_7.png" class="w-full h-full object-cover"></div>
                                    <div>
                                        <p class="font-semibold text-slate-900 text-sm">Dynamic Thread</p>
                                        <p class="text-sm text-slate-600 mt-1">When you tilt from top to bottom, the Security Thread shows dynamic effect.</p>
                                    </div>
                                </li>
                                <li class="flex gap-4 items-start">
                                    <div class="w-16 h-16 shrink-0 rounded-lg overflow-hidden border border-slate-200 bg-white"><img src="https://www.nrb.org.np/contents/uploads/2020/11/1000_9.png" class="w-full h-full object-cover"></div>
                                    <div>
                                        <p class="font-semibold text-slate-900 text-sm">Iridescent Ink</p>
                                        <p class="text-sm text-slate-600 mt-1">When you tilt the banknote, the iridescent effect is clearly visible.</p>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</section>
"""

with open(notes_html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the dummy document grid with the new rich content layout
html_content = re.sub(r'<section class="py-14 border-b border-slate-200 bg-slate-50" id="documents">.*?</section>', notes_content, html_content, flags=re.DOTALL)

with open(notes_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated Know Your Bank Notes.")
