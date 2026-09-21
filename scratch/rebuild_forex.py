import os
import re

forex_path = 'c:/Users/LOQ/Desktop/NRB Redesign/pages/forex-management/index.html'

with open(forex_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Split around <main... and </main>
parts = re.split(r'<main[^>]*>.*?</main>', content, flags=re.DOTALL)

if len(parts) != 2:
    print("Could not find <main> tag correctly.")
    exit(1)

header_html = parts[0]
footer_html = parts[1]

# Correct the page title
header_html = re.sub(r'<title>.*?</title>', '<title>Daily Exchange Rate | NRB</title>', header_html, flags=re.DOTALL)

main_html = """
<main>
    <!-- HERO -->
    <section class="border-b border-slate-200 bg-white">
        <div class="nrb-section-shell py-10 lg:py-14">
            <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
                <a class="transition hover:text-[#25295B]" href="../../nrb.html">Home</a>
                <span class="text-slate-300">/</span>
                <a class="transition hover:text-[#25295B]" href="../../pages/statistics/index.html">Statistics</a>
                <span class="text-slate-300">/</span>
                <a class="transition hover:text-[#25295B]" href="../../pages/statistics/monetary-forex/index.html">Monetary & Forex Statistics</a>
                <span class="text-slate-300">/</span>
                <span class="text-slate-700">Foreign Exchange</span>
            </nav>
            <h1 class="text-2xl font-bold text-slate-900 mb-3">Daily Exchange Rate</h1>
            <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Live exchange rates and reserve updates for foreign currencies. Showing Exchange Rate for September 21, 2026.</p>
        </div>
    </section>

    <section class="bg-slate-50 py-14 border-b border-slate-200">
        <div class="nrb-section-shell">
            
            <!-- FIXED RATES -->
            <div class="mb-10">
                <header class="mb-6">
                    <h2 class="text-xl font-bold text-slate-900">Fixed By Nepal Rastra Bank</h2>
                    <p class="mt-1 text-sm text-slate-600">Fixed exchange rates against the Indian Rupee.</p>
                </header>
                
                <div class="overflow-hidden rounded-[20px] border border-slate-200 bg-white shadow-sm">
                    <table class="w-full border-collapse text-left">
                        <thead class="bg-slate-100">
                            <tr class="border-b border-slate-200 text-xs uppercase tracking-[0.16em] text-slate-500">
                                <th class="px-6 py-4 font-semibold">Currency</th>
                                <th class="px-6 py-4 font-semibold text-center">Unit</th>
                                <th class="px-6 py-4 font-semibold text-right">Buy Rate (NPR)</th>
                                <th class="px-6 py-4 font-semibold text-right">Sell Rate (NPR)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200">
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-semibold text-slate-900">INR (Indian Rupee)</td>
                                <td class="px-6 py-4 text-center">100</td>
                                <td class="px-6 py-4 text-right">160.00</td>
                                <td class="px-6 py-4 text-right">160.15</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- OPEN MARKET RATES -->
            <div>
                <header class="mb-6 flex items-end justify-between">
                    <div>
                        <h2 class="text-xl font-bold text-slate-900">Open Market Exchange Rates</h2>
                        <p class="mt-1 text-sm text-slate-600">For the purpose of Nepal Rastra Bank.</p>
                    </div>
                </header>
                
                <div class="overflow-hidden rounded-[20px] border border-slate-200 bg-white shadow-sm">
                    <table class="w-full border-collapse text-left">
                        <thead class="bg-slate-100">
                            <tr class="border-b border-slate-200 text-xs uppercase tracking-[0.16em] text-slate-500">
                                <th class="px-6 py-4 font-semibold">Currency</th>
                                <th class="px-6 py-4 font-semibold text-center">Unit</th>
                                <th class="px-6 py-4 font-semibold text-right">Buy Rate (NPR)</th>
                                <th class="px-6 py-4 font-semibold text-right">Sell Rate (NPR)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200">
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-semibold text-slate-900 flex items-center gap-2">
                                    <span class="w-6 h-6 rounded-full bg-slate-100 flex items-center justify-center text-[10px]">🇺🇸</span>
                                    USD (U.S. Dollar)
                                </td>
                                <td class="px-6 py-4 text-center">1</td>
                                <td class="px-6 py-4 text-right">133.42</td>
                                <td class="px-6 py-4 text-right">133.96</td>
                            </tr>
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-semibold text-slate-900 flex items-center gap-2">
                                    <span class="w-6 h-6 rounded-full bg-slate-100 flex items-center justify-center text-[10px]">🇪🇺</span>
                                    EUR (European Euro)
                                </td>
                                <td class="px-6 py-4 text-center">1</td>
                                <td class="px-6 py-4 text-right">146.28</td>
                                <td class="px-6 py-4 text-right">146.87</td>
                            </tr>
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-semibold text-slate-900 flex items-center gap-2">
                                    <span class="w-6 h-6 rounded-full bg-slate-100 flex items-center justify-center text-[10px]">🇬🇧</span>
                                    GBP (UK Pound Sterling)
                                </td>
                                <td class="px-6 py-4 text-center">1</td>
                                <td class="px-6 py-4 text-right">170.22</td>
                                <td class="px-6 py-4 text-right">170.92</td>
                            </tr>
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-semibold text-slate-900 flex items-center gap-2">
                                    <span class="w-6 h-6 rounded-full bg-slate-100 flex items-center justify-center text-[10px]">🇦🇺</span>
                                    AUD (Australian Dollar)
                                </td>
                                <td class="px-6 py-4 text-center">1</td>
                                <td class="px-6 py-4 text-right">88.61</td>
                                <td class="px-6 py-4 text-right">89.00</td>
                            </tr>
                            <tr class="text-sm text-slate-700 hover:bg-slate-50 transition-colors">
                                <td class="px-6 py-4 font-semibold text-slate-900 flex items-center gap-2">
                                    <span class="w-6 h-6 rounded-full bg-slate-100 flex items-center justify-center text-[10px]">🇯🇵</span>
                                    JPY (Japanese Yen)
                                </td>
                                <td class="px-6 py-4 text-center">10</td>
                                <td class="px-6 py-4 text-right">9.02</td>
                                <td class="px-6 py-4 text-right">9.06</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
        </div>
    </section>
</main>
"""

new_full_html = header_html + '\n' + main_html + '\n' + footer_html

with open(forex_path, 'w', encoding='utf-8') as f:
    f.write(new_full_html)
print("Rebuilt Forex page.")
