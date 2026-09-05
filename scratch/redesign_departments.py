import os

html_content = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="view-transition" content="same-origin" />
    <title>Departments, Divisions & Units | Nepal Rastra Bank</title>
    <meta name="description" content="Official directory of departments, divisions, and specialized units of Nepal Rastra Bank." />
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../../assets/css/nrb-core.css" />
    <style>
        .hub-card { transition: border-color 200ms ease, box-shadow 200ms ease, background-color 200ms ease; }
        .hub-card:hover { border-color: rgba(30, 58, 95, 0.2); box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05); }
        .about-local-nav a {
            position: relative; padding-bottom: 4px; font-size: 0.875rem;
            font-weight: 500; color: #64748B; text-decoration: none;
            white-space: nowrap; transition: color 150ms;
        }
        .about-local-nav a::after {
            content: ''; position: absolute; bottom: -1px; left: 0; right: 0;
            height: 2px; background: transparent; border-radius: 2px; transition: background 150ms;
        }
        .about-local-nav a:hover { color: #25295B; }
        .about-local-nav a[aria-current="page"] { color: #25295B; font-weight: 600; }
        .about-local-nav a[aria-current="page"]::after { background: #25295B; }
        
        .filter-btn { transition: all 150ms ease; }
        .filter-btn.active {
            background-color: #25295B;
            color: #FFFFFF;
            border-color: #25295B;
        }
    </style>
</head>
<body class="min-w-[1440px] bg-slate-50 text-slate-900 antialiased font-['Inter',sans-serif]">
    <div class="nrb-page-frame mx-auto w-full max-w-[1440px]">

        <!-- GLOBAL HEADER -->
        <header id="Site-Header" class="bg-[#25295B] text-white shadow-sm">
            <div class="border-b border-white/10">
                <div class="nrb-section-shell flex items-center justify-between py-6">
                    <a id="Brand-Mark" href="../../nrb.html" class="flex items-center gap-4">
                        <div class="flex h-14 w-14 items-center justify-center rounded-full overflow-hidden bg-white shadow-sm">
                            <img src="../../assets/images/nrb-logo.png" alt="Nepal Rastra Bank Official Seal" class="h-13 w-13 object-contain" />
                        </div>
                        <div class="flex flex-col">
                            <span class="text-xs font-semibold uppercase tracking-[0.24em] text-slate-200">Nepal Rastra Bank</span>
                            <span class="text-sm text-slate-300">Central Bank of Nepal</span>
                        </div>
                    </a>
                    <div class="flex items-center gap-4 text-xs font-semibold uppercase tracking-wider text-slate-200">
                        <a href="#" class="transition hover:text-white">EN / NEP</a>
                    </div>
                </div>
            </div>
            <div id="Main-Header">
                <div class="nrb-section-shell py-4">
                    <nav id="Primary-Navigation" aria-label="Primary" class="flex items-center justify-between text-sm font-medium">
                        <div class="relative group">
                            <a id="Nav-About-NRB" href="../../pages/about/index.html" class="flex items-center gap-1.5 text-white border-b-2 border-white pb-0.5">
                                About NRB
                                <svg class="w-3.5 h-3.5 transition-transform duration-200 group-hover:rotate-180" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7"></path></svg>
                            </a>
                            <div class="absolute left-0 top-full pt-4 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50">
                                <div class="bg-white rounded-[20px] shadow-lg border border-slate-200 py-3 w-64 flex flex-col">
                                    <a href="../../pages/about/index.html#overview" class="px-5 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Institution Overview</a>
                                    <a href="../../pages/about/index.html#leadership" class="px-5 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Leadership &amp; Governance</a>
                                    <a href="../../pages/about/index.html#organization" class="px-5 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Organizational Structure</a>
                                    <a href="../../pages/about/index.html#offices" class="px-5 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Offices &amp; Network</a>
                                    <a href="../../pages/about/index.html#statements" class="px-5 py-2.5 text-sm text-slate-700 hover:bg-slate-50 hover:text-[#138496] font-medium transition-colors">Financial Statements</a>
                                </div>
                            </div>
                        </div>
                        <a id="Nav-Monetary-Policy" href="../../pages/monetary-policy/index.html" class="text-slate-100 transition hover:text-[#138496]">Monetary Policy</a>
                        <a id="Nav-Bank-Supervision" href="../../pages/bank-supervision/index.html" class="text-slate-100 transition hover:text-[#138496]">Bank Supervision</a>
                        <a id="Nav-Forex-Management" href="../../pages/forex-management/index.html" class="text-slate-100 transition hover:text-[#138496]">Forex Management</a>
                        <a id="Nav-Statistics" href="../../pages/statistics/index.html" class="text-slate-100 transition hover:text-[#138496]">Statistics</a>
                        <a id="Nav-Publications" href="../../pages/publications/index.html" class="text-slate-100 transition hover:text-[#138496]">Publications</a>
                        <a id="Nav-Notices" href="../../pages/notices/index.html" class="text-slate-100 transition hover:text-[#138496]">Notices</a>
                        <a id="Nav-Careers" href="../../pages/careers/index.html" class="text-slate-100 transition hover:text-[#138496]">Careers</a>
                        <a id="Nav-Contact" href="../../pages/contact/index.html" class="text-slate-100 transition hover:text-[#138496]">Contact</a>
                    </nav>
                </div>
            </div>
        </header>

        <main>
            <!-- HERO -->
            <section class="border-b border-slate-200 bg-white">
                <div class="nrb-section-shell py-10 lg:py-14">
                    <nav aria-label="Breadcrumb" class="mb-6 flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-slate-500">
                        <a href="../../nrb.html" class="transition hover:text-[#25295B]">Home</a>
                        <span class="text-slate-300">/</span>
                        <a href="index.html" class="transition hover:text-[#25295B]">About NRB</a>
                        <span class="text-slate-300">/</span>
                        <a href="index.html#organization" class="transition hover:text-[#25295B]">Organization</a>
                        <span class="text-slate-300">/</span>
                        <span class="text-slate-700">Departments, Divisions &amp; Units</span>
                    </nav>
                    
                    <div class="mb-5">
                        <a href="index.html" class="inline-flex items-center gap-2 text-sm font-semibold text-[#138496] transition-colors hover:text-[#1E3A5F]">
                            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18" /></svg>
                            Back to About Overview
                        </a>
                    </div>
                    <h1 class="nrb-page-title text-[#1E3A5F] mb-4">Departments, Divisions &amp; Units</h1>
                    <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Official directory of Nepal Rastra Bank's specialized departments, operational divisions, and autonomous units responsible for central banking governance, policy, regulation, and public administration.</p>
                </div>
            </section>

            <!-- ORGANIZATION NAVIGATION STRIP -->
            <div class="border-b border-slate-200 bg-white sticky top-0 z-20 shadow-sm">
                <div class="nrb-section-shell">
                    <nav class="about-local-nav flex items-center gap-8 py-4" aria-label="Organization navigation">
                        <a href="organogram.html">Organogram</a>
                        <a href="departments.html" aria-current="page">Departments &amp; Divisions</a>
                        <a href="provincial-offices.html">Provincial Offices</a>
                    </nav>
                </div>
            </div>

            <!-- CONTROLS & FILTER BAR -->
            <section class="bg-white border-b border-slate-200 py-6">
                <div class="nrb-section-shell">
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <!-- Category Tabs -->
                        <div class="flex flex-wrap items-center gap-2">
                            <button onclick="filterCategory('all')" id="tab-all" class="filter-btn active px-4 py-2 rounded-full text-xs font-semibold border border-slate-200 bg-[#25295B] text-white">All Entities (25)</button>
                            <button onclick="filterCategory('office')" id="tab-office" class="filter-btn px-4 py-2 rounded-full text-xs font-semibold border border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100">Executive Office (1)</button>
                            <button onclick="filterCategory('department')" id="tab-department" class="filter-btn px-4 py-2 rounded-full text-xs font-semibold border border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100">Departments (17)</button>
                            <button onclick="filterCategory('division')" id="tab-division" class="filter-btn px-4 py-2 rounded-full text-xs font-semibold border border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100">Divisions (6)</button>
                            <button onclick="filterCategory('unit')" id="tab-unit" class="filter-btn px-4 py-2 rounded-full text-xs font-semibold border border-slate-200 bg-slate-50 text-slate-700 hover:bg-slate-100">Specialized Unit (1)</button>
                        </div>

                        <!-- Search Bar -->
                        <div class="relative w-full md:w-80">
                            <svg class="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
                            <input type="text" id="dept-search" oninput="searchDirectory()" placeholder="Search directory..." class="w-full pl-10 pr-4 py-2 text-xs rounded-full border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#138496]/20 focus:border-[#138496] transition-all" />
                        </div>
                    </div>
                </div>
            </section>

            <!-- MAIN DIRECTORY GRID -->
            <section class="bg-slate-50 py-12">
                <div class="nrb-section-shell">
                    
                    <div id="dept-grid" class="grid grid-cols-2 gap-6">

                        <!-- 1. Office of the Governor -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="office" data-name="office of the governor executive secretariat board">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Executive Office</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Office of the Governor</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Executive secretariat managing official communications, board governance, policy workflows, and central bank administration under the Governor.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:ofg@nrb.org.np" class="text-[#138496] font-medium hover:underline">ofg@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5719600, 5719601</span>
                                </div>
                            </div>
                        </div>

                        <!-- 2. Economic Research Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="economic research department monetary policy macroeconomics inflation statistics">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Economic Research Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Macroeconomic analysis, monetary policy formulation, inflation tracking, trade statistics, and economic policy research.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:research@nrb.org.np" class="text-[#138496] font-medium hover:underline">research@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1406)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 3. Banks & Financial Institutions Regulation Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="banks financial institutions regulation department bfr directives licensing prudential">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Banks &amp; Financial Institutions Regulation Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Formulation of regulatory directives, capital adequacy frameworks, prudential norms, and licensing policies for BFIs.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:bfr@nrb.org.np" class="text-[#138496] font-medium hover:underline">bfr@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5719614, 5719613</span>
                                </div>
                            </div>
                        </div>

                        <!-- 4. Foreign Exchange Management Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="foreign exchange management department fx forex reserve cross-border">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Foreign Exchange Management Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Foreign exchange reserve management, exchange rate policy, capital account monitoring, and cross-border payment regulations.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:fxm@nrb.org.np" class="text-[#138496] font-medium hover:underline">fxm@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1510)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 5. Currency Management Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="currency management department banknote cash printing vault clean note">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Thapathali, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Currency Management Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Banknote printing, currency vault operations, clean note policy implementation, and distribution across provincial offices.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:cmd@nrb.org.np" class="text-[#138496] font-medium hover:underline">cmd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5925570 (Ext. 3206)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 6. Financial Management Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="financial management department accounting budget reports fmd">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Financial Management Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Central bank accounting, financial statements preparation, statutory budgeting, financial controls, and fiscal operations.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:fmd@nrb.org.np" class="text-[#138496] font-medium hover:underline">fmd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1310)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 7. Human Resources Management Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="human resources management department hrm recruitment staffing career">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Human Resources Management Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Staff recruitment, career progression, employee benefits, organizational development, and central bank personnel policy.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:hrmd@nrb.org.np" class="text-[#138496] font-medium hover:underline">hrmd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1220)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 8. Internal Audit Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="internal audit department iad compliance risk control">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Internal Audit Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Independent audit reviews, compliance monitoring, operational risk assessment, and internal control effectiveness evaluations.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:iad@nrb.org.np" class="text-[#138496] font-medium hover:underline">iad@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5719627</span>
                                </div>
                            </div>
                        </div>

                        <!-- 9. Assets and Service Management Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="assets service management department procurement property gsd logistics">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Assets and Service Management Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Institutional procurement, physical infrastructure development, facility management, and logistics support.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:gsd@nrb.org.np" class="text-[#138496] font-medium hover:underline">gsd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1180)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 10. Monetary Management Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="monetary management department liquidity open market treasury bills mmd">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Thapathali, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Monetary Management Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Open market operations, liquidity management, treasury bill auctions, standing liquidity facilities, and interbank operations.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:mmd@nrb.org.np" class="text-[#138496] font-medium hover:underline">mmd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5925572 (Ext. 3315)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 11. Microfinance Institutions Supervision Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="microfinance institutions supervision department mfd class d supervision">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Microfinance Institutions Supervision Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">On-site and off-site prudential supervision of Class 'D' microfinance financial institutions nationwide.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:mfd@nrb.org.np" class="text-[#138496] font-medium hover:underline">mfd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5719630, 5719628</span>
                                </div>
                            </div>
                        </div>

                        <!-- 12. Bank Supervision Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="bank supervision department commercial banks bsd class a supervision">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Bank Supervision Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Comprehensive on-site inspection and off-site prudential supervision of Class 'A' commercial banks in Nepal.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:bsd@nrb.org.np" class="text-[#138496] font-medium hover:underline">bsd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 2207)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 13. Corporate Planning and Risk Management Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="corporate planning risk management department strategy cpd enterprise risk">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Corporate Planning &amp; Risk Management Dept.</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Strategic institutional planning, enterprise risk governance, policy evaluation, and corporate performance monitoring.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:corporate@nrb.org.np" class="text-[#138496] font-medium hover:underline">corporate@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1383)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 14. Information Technology Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="information technology department itd core banking cybersecurity rtgs">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Information Technology Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Core banking systems, RTGS infrastructure, enterprise cybersecurity, IT governance, and digital network administration.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:itdept@nrb.org.np" class="text-[#138496] font-medium hover:underline">itdept@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5719641 (Ext. 2557)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 15. Payment Systems Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="payment systems department digital payments psd pso psp fintech">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Payment Systems Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Regulation, licensing, and oversight of payment systems, clearing houses, payment service operators (PSOs), and PSPs.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:psdept@nrb.org.np" class="text-[#138496] font-medium hover:underline">psdept@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1349)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 16. Non-Bank Financial Institutions Supervision Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="non-bank financial institutions supervision department nbfisd cooperatives hire purchase">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Non-Bank Financial Institutions Supervision Dept.</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Supervision and regulatory compliance of hire-purchase entities, specialized non-bank financial intermediaries, and funds.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:nbfisd@nrb.org.np" class="text-[#138496] font-medium hover:underline">nbfisd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 2326)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 17. Financial Institutions Supervision Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="financial institutions supervision department fisd development banks finance companies class b class c">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Financial Institutions Supervision Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">On-site and off-site prudential supervision of Class 'B' development banks and Class 'C' finance companies.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:nrbfisd@nrb.org.np" class="text-[#138496] font-medium hover:underline">nrbfisd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5719636</span>
                                </div>
                            </div>
                        </div>

                        <!-- 18. Banking Department -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="department" data-name="banking department government accounts treasury debt public">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Department</span>
                                    <span class="text-xs text-slate-500 font-medium">Thapathali, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Banking Department</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Government banking services, central bank accounts management, public debt servicing, and banking operations.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:banking@nrb.org.np" class="text-[#138496] font-medium hover:underline">banking@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5925572</span>
                                </div>
                            </div>
                        </div>

                        <!-- 19. Bankers’ Training Centre -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="division" data-name="bankers training centre division btc education development">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Division</span>
                                    <span class="text-xs text-slate-500 font-medium">Thapathali, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Bankers’ Training Centre</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Professional training, central banking certification programs, and executive leadership development for financial institutions.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:btc@nrb.org.np" class="text-[#138496] font-medium hover:underline">btc@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5925566</span>
                                </div>
                            </div>
                        </div>

                        <!-- 20. Legal Division -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="division" data-name="legal division legislative drafting court litigation counsel">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Division</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Legal Division</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Central bank legal advice, legislative drafting, statutory compliance, and representation in judicial proceedings.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:legal@nrb.org.np" class="text-[#138496] font-medium hover:underline">legal@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1251)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 21. Mint Division -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="division" data-name="mint division coin medals bullion assaying">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Division</span>
                                    <span class="text-xs text-slate-500 font-medium">Babarmahal, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Mint Division</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Coin minting, commemorative medals crafting, bullion assaying, and official precious metals verification.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:mint@nrb.org.np" class="text-[#138496] font-medium hover:underline">mint@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-4102134, 4102136</span>
                                </div>
                            </div>
                        </div>

                        <!-- 22. Financial Inclusion and Consumer Protection Division -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="division" data-name="financial inclusion consumer protection division ficpd grievance literacy">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Division</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Financial Inclusion &amp; Consumer Protection Division</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Financial literacy initiatives, financial access expansion, and consumer grievance redressal mechanisms.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:ficpd@nrb.org.np" class="text-[#138496] font-medium hover:underline">ficpd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 2366)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 23. Money Laundering Prevention Supervision Division -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="division" data-name="money laundering prevention supervision division mlpsd aml cft compliance">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Division</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Money Laundering Prevention Supervision Division</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Anti-Money Laundering and Countering Financing of Terrorism (AML/CFT) supervision across financial institutions.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:mlpsd@nrb.org.np" class="text-[#138496] font-medium hover:underline">mlpsd@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 2275)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 24. Statistics Division -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="division" data-name="statistics division macroeconomic data dissemination indicators">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Division</span>
                                    <span class="text-xs text-slate-500 font-medium">Baluwatar, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Statistics Division</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">Compilation, processing, and public dissemination of national macroeconomic indicators and banking sector data.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:statistics@nrb.org.np" class="text-[#138496] font-medium hover:underline">statistics@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-1-5719641 (Ext. 1421)</span>
                                </div>
                            </div>
                        </div>

                        <!-- 25. Financial Intelligence Unit -->
                        <div class="dept-item hub-card bg-white rounded-[20px] border border-slate-200 p-7 flex flex-col justify-between" data-category="unit" data-name="financial intelligence unit fiu autonomous str suspicious transactions">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-semibold uppercase tracking-wider">Specialized Unit</span>
                                    <span class="text-xs text-slate-500 font-medium">Thapathali, Kathmandu</span>
                                </div>
                                <h3 class="text-lg font-bold text-slate-900 mb-1.5">Financial Intelligence Unit (FIU-Nepal)</h3>
                                <p class="text-sm text-slate-600 leading-relaxed mb-4">The central national agency responsible for receiving, analyzing, and disseminating financial intelligence related to suspicious transactions.</p>
                            </div>
                            <div class="pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-600">
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Email:</span>
                                    <a href="mailto:fiu@nrb.org.np" class="text-[#138496] font-medium hover:underline">fiu@nrb.org.np</a>
                                </div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-semibold text-slate-900">Phone:</span>
                                    <span>+977-01-5925571</span>
                                </div>
                            </div>
                        </div>

                    </div>

                    <!-- No results state -->
                    <div id="no-results" class="hidden text-center py-16 bg-white rounded-[20px] border border-slate-200">
                        <p class="text-base font-semibold text-slate-700">No departments or divisions match your search.</p>
                        <p class="text-sm text-slate-400 mt-1">Try searching with a different keyword or reset the category filter.</p>
                    </div>

                </div>
            </section>
        </main>

        <!-- GLOBAL FOOTER -->
        <footer id="Footer" class="nrb-footer bg-[#25295B] text-white">
            <div class="nrb-section-shell py-16">
                <div class="flex flex-col gap-6 border-b border-white/10 pb-10">
                    <div class="flex items-center gap-4">
                        <div class="flex h-12 w-12 items-center justify-center rounded-full overflow-hidden bg-white shadow-sm">
                            <img src="../../assets/images/nrb-logo.png" alt="Nepal Rastra Bank Official Seal" class="h-11 w-11 object-contain" />
                        </div>
                        <div>
                            <p class="text-sm font-semibold uppercase tracking-[0.22em] text-slate-200">Nepal Rastra Bank</p>
                            <p class="mt-1 text-sm text-slate-300">Central Bank of Nepal</p>
                        </div>
                    </div>
                    <p class="max-w-3xl text-sm leading-6 text-slate-300">
                        The official digital headquarters for Nepal's central bank, bringing together monetary policy, economic data, financial regulation, research publications, notices, and public services in one authoritative portal.
                    </p>
                </div>
                <div class="mt-10 grid grid-cols-5 gap-8">
                    <div class="flex flex-col gap-4">
                        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-200">About NRB</h3>
                        <a href="../../pages/about/index.html" class="text-sm text-slate-300 transition hover:text-white">Overview</a>
                        <a href="../../pages/about/index.html#leadership" class="text-sm text-slate-300 transition hover:text-white">Leadership</a>
                        <a href="../../pages/about/index.html#organization" class="text-sm text-slate-300 transition hover:text-white">Departments</a>
                        <a href="../../pages/about/index.html#offices" class="text-sm text-slate-300 transition hover:text-white">Offices</a>
                    </div>
                    <div class="flex flex-col gap-4">
                        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-200">Statistics &amp; Data</h3>
                        <a href="../../pages/statistics/index.html" class="text-sm text-slate-300 transition hover:text-white">Economic indicators</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Exchange rates</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Financial stability</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Open data</a>
                    </div>
                    <div class="flex flex-col gap-4">
                        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-200">Publications</h3>
                        <a href="../../pages/publications/index.html" class="text-sm text-slate-300 transition hover:text-white">Reports</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Research</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Working papers</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Annual reports</a>
                    </div>
                    <div class="flex flex-col gap-4">
                        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-200">Consumer Services</h3>
                        <a href="../../pages/consumer-services/index.html" class="text-sm text-slate-300 transition hover:text-white">Consumer protection</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Complaints</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">Financial literacy</a>
                        <a href="#" class="text-sm text-slate-300 transition hover:text-white">FAQ</a>
                    </div>
                    <div class="flex flex-col gap-4">
                        <h3 class="text-sm font-semibold uppercase tracking-[0.18em] text-slate-200">Contact</h3>
                        <p class="text-sm leading-6 text-slate-300">Baluwatar, Kathmandu, Nepal</p>
                        <p class="text-sm leading-6 text-slate-300">Phone: +977-1-4419804</p>
                        <p class="text-sm leading-6 text-slate-300">Email: info@nrb.org.np</p>
                        <p class="text-sm leading-6 text-slate-300">Provincial offices available nationwide</p>
                    </div>
                </div>
                <div class="mt-10 flex flex-wrap items-center justify-between gap-4 border-t border-white/10 pt-6 text-sm text-slate-400">
                    <p>© 2026 Nepal Rastra Bank. All rights reserved.</p>
                    <div class="flex flex-wrap items-center gap-5">
                        <a href="#" class="transition hover:text-white">Privacy Policy</a>
                        <a href="#" class="transition hover:text-white">Accessibility</a>
                        <a href="#" class="transition hover:text-white">Terms of Use</a>
                        <a href="#Footer" class="transition hover:text-white">Sitemap</a>
                    </div>
                </div>
            </div>
        </footer>
    </div>

    <!-- Interactivity Script for Filtering & Search -->
    <script>
        let currentCat = 'all';

        function filterCategory(cat) {
            currentCat = cat;
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active', 'bg-[#25295B]', 'text-white');
                btn.classList.add('bg-slate-50', 'text-slate-700');
            });
            const activeBtn = document.getElementById('tab-' + cat);
            if (activeBtn) {
                activeBtn.classList.add('active', 'bg-[#25295B]', 'text-white');
                activeBtn.classList.remove('bg-slate-50', 'text-slate-700');
            }
            applyFilters();
        }

        function searchDirectory() {
            applyFilters();
        }

        function applyFilters() {
            const query = document.getElementById('dept-search').value.toLowerCase().trim();
            const items = document.querySelectorAll('.dept-item');
            let visibleCount = 0;

            items.forEach(item => {
                const itemCat = item.getAttribute('data-category');
                const itemName = item.getAttribute('data-name');
                const matchesCat = (currentCat === 'all' || itemCat === currentCat);
                const matchesSearch = !query || itemName.includes(query) || item.innerText.toLowerCase().includes(query);

                if (matchesCat && matchesSearch) {
                    item.classList.remove('hidden');
                    visibleCount++;
                } else {
                    item.classList.add('hidden');
                }
            });

            const noResults = document.getElementById('no-results');
            if (noResults) {
                if (visibleCount === 0) {
                    noResults.classList.remove('hidden');
                } else {
                    noResults.classList.add('hidden');
                }
            }
        }
    </script>
</body>

</html>'''

with open('pages/about/departments.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Redesigned departments.html cleanly without clutter or AI boxes!")
