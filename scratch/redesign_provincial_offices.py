import os

html_content = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="view-transition" content="same-origin" />
    <title>Provincial Offices | Nepal Rastra Bank</title>
    <meta name="description" content="Official directory and network of Nepal Rastra Bank provincial offices across Koshi, Madhesh, Gandaki, Lumbini, Karnali, and Sudurpashchim provinces." />
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../../assets/css/nrb-core.css" />
    <style>
        .hub-card { transition: transform 150ms ease, box-shadow 150ms ease, border-color 150ms ease; }
        .hub-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(15,23,42,0.08); }
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
    </style>
</head>
<body class="min-w-[1440px] bg-slate-50 text-slate-900 antialiased">
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
                        <span class="text-slate-700">Provincial Offices</span>
                    </nav>
                    
                    <div class="mb-5">
                        <a href="index.html" class="inline-flex items-center gap-2 text-sm font-semibold text-[#138496] transition-colors hover:text-[#1E3A5F]">
                            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18" /></svg>
                            Back to About Overview
                        </a>
                    </div>
                    <h1 class="nrb-page-title text-[#1E3A5F] mb-4">Provincial Offices Network</h1>
                    <p class="text-base text-slate-600 leading-relaxed max-w-2xl">Nepal Rastra Bank maintains seven provincial offices strategically located across Nepal's provinces, extending central banking, currency management, supervisory oversight, and public treasury services nationwide.</p>
                </div>
            </section>

            <!-- ORGANIZATION NAVIGATION STRIP -->
            <div class="border-b border-slate-200 bg-white sticky top-0 z-20 shadow-sm">
                <div class="nrb-section-shell">
                    <nav class="about-local-nav flex items-center gap-8 py-4" aria-label="Organization navigation">
                        <a href="organogram.html">Organogram</a>
                        <a href="departments.html">Departments &amp; Divisions</a>
                        <a href="provincial-offices.html" aria-current="page">Provincial Offices</a>
                    </nav>
                </div>
            </div>

            <!-- NETWORK OVERVIEW STATS -->
            <section class="bg-slate-50 py-14 border-b border-slate-200">
                <div class="nrb-section-shell">
                    <div class="mb-8">
                        <p class="nrb-display-note">Nationwide Infrastructure</p>
                        <h2 class="nrb-section-title mt-1 text-slate-900">Regional Banking &amp; Treasury Network</h2>
                        <p class="text-sm text-slate-500 mt-1">Empowered branch offices serving government agencies, banking institutions, and the public across all 7 provinces.</p>
                    </div>

                    <div class="grid grid-cols-4 gap-6 mb-12">
                        <div class="bg-white rounded-[20px] border border-slate-200 p-6 text-center shadow-sm">
                            <p class="text-3xl font-bold text-[#25295B] mb-1">7</p>
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-500">Provincial Offices</p>
                        </div>
                        <div class="bg-white rounded-[20px] border border-slate-200 p-6 text-center shadow-sm">
                            <p class="text-3xl font-bold text-[#25295B] mb-1">77</p>
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-500">Districts Served</p>
                        </div>
                        <div class="bg-white rounded-[20px] border border-slate-200 p-6 text-center shadow-sm">
                            <p class="text-3xl font-bold text-[#25295B] mb-1">100%</p>
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-500">Currency Distribution</p>
                        </div>
                        <div class="bg-white rounded-[20px] border border-slate-200 p-6 text-center shadow-sm">
                            <p class="text-3xl font-bold text-[#25295B] mb-1">24/7</p>
                            <p class="text-xs font-semibold uppercase tracking-wider text-slate-500">Treasury Clearing</p>
                        </div>
                    </div>

                    <!-- PROVINCIAL OFFICE DIRECTORY GRID -->
                    <div class="mb-6 flex items-center justify-between">
                        <h3 class="text-xl font-bold text-slate-900">Provincial Office Directory</h3>
                        <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">7 Regional Branches</span>
                    </div>

                    <div class="grid grid-cols-2 gap-6">
                        
                        <!-- 1. Biratnagar -->
                        <div class="hub-card bg-white rounded-[20px] border border-slate-200 p-8 shadow-sm hover:border-[#1E3A5F]/20 transition-all flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-4">
                                    <span class="inline-flex items-center rounded-full bg-slate-100 px-3.5 py-1 text-xs font-semibold text-[#25295B]">Koshi Province</span>
                                    <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md">Operational</span>
                                </div>
                                <h4 class="text-xl font-bold text-slate-900 mb-2">Biratnagar Office</h4>
                                <p class="text-sm text-slate-500 leading-relaxed mb-6">Manages currency chests, government accounts, and supervisory oversight for financial institutions across Koshi Province.</p>
                                
                                <div class="space-y-3 text-sm text-slate-600 border-t border-slate-100 pt-5">
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Address</p>
                                            <p class="text-slate-600">Main Road, Biratnagar, Morang</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Telephone</p>
                                            <p class="text-slate-600">+977-21-525284 / +977-21-525285</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Email</p>
                                            <p class="text-[#138496] font-medium">biratnagar@nrb.org.np</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 2. Janakpur -->
                        <div class="hub-card bg-white rounded-[20px] border border-slate-200 p-8 shadow-sm hover:border-[#1E3A5F]/20 transition-all flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-4">
                                    <span class="inline-flex items-center rounded-full bg-slate-100 px-3.5 py-1 text-xs font-semibold text-[#25295B]">Madhesh Province</span>
                                    <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md">Operational</span>
                                </div>
                                <h4 class="text-xl font-bold text-slate-900 mb-2">Janakpur Office</h4>
                                <p class="text-sm text-slate-500 leading-relaxed mb-6">Provides currency distribution, government transaction clearing, and regulatory support for Madhesh Province.</p>
                                
                                <div class="space-y-3 text-sm text-slate-600 border-t border-slate-100 pt-5">
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Address</p>
                                            <p class="text-slate-600">Station Road, Janakpurdham, Dhanusha</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Telephone</p>
                                            <p class="text-slate-600">+977-41-524250 / +977-41-524251</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Email</p>
                                            <p class="text-[#138496] font-medium">janakpur@nrb.org.np</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 3. Pokhara -->
                        <div class="hub-card bg-white rounded-[20px] border border-slate-200 p-8 shadow-sm hover:border-[#1E3A5F]/20 transition-all flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-4">
                                    <span class="inline-flex items-center rounded-full bg-slate-100 px-3.5 py-1 text-xs font-semibold text-[#25295B]">Gandaki Province</span>
                                    <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md">Operational</span>
                                </div>
                                <h4 class="text-xl font-bold text-slate-900 mb-2">Pokhara Office</h4>
                                <p class="text-sm text-slate-500 leading-relaxed mb-6">Executes foreign exchange clearances, banking supervision, and treasury management for Gandaki Province.</p>
                                
                                <div class="space-y-3 text-sm text-slate-600 border-t border-slate-100 pt-5">
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Address</p>
                                            <p class="text-slate-600">Rastra Bank Chowk, Pokhara, Kaski</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Telephone</p>
                                            <p class="text-slate-600">+977-61-520355 / +977-61-520356</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Email</p>
                                            <p class="text-[#138496] font-medium">pokhara@nrb.org.np</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 4. Siddharthanagar -->
                        <div class="hub-card bg-white rounded-[20px] border border-slate-200 p-8 shadow-sm hover:border-[#1E3A5F]/20 transition-all flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-4">
                                    <span class="inline-flex items-center rounded-full bg-slate-100 px-3.5 py-1 text-xs font-semibold text-[#25295B]">Lumbini Province</span>
                                    <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md">Operational</span>
                                </div>
                                <h4 class="text-xl font-bold text-slate-900 mb-2">Siddharthanagar Office</h4>
                                <p class="text-sm text-slate-500 leading-relaxed mb-6">Facilitates border trade currency settlement, public treasury operations, and banking supervision in Lumbini Province.</p>
                                
                                <div class="space-y-3 text-sm text-slate-600 border-t border-slate-100 pt-5">
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Address</p>
                                            <p class="text-slate-600">Bank Road, Siddharthanagar, Rupandehi</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Telephone</p>
                                            <p class="text-slate-600">+977-71-520128 / +977-71-520129</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Email</p>
                                            <p class="text-[#138496] font-medium">bhairahawa@nrb.org.np</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 5. Nepalgunj -->
                        <div class="hub-card bg-white rounded-[20px] border border-slate-200 p-8 shadow-sm hover:border-[#1E3A5F]/20 transition-all flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-4">
                                    <span class="inline-flex items-center rounded-full bg-slate-100 px-3.5 py-1 text-xs font-semibold text-[#25295B]">Lumbini Province</span>
                                    <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md">Operational</span>
                                </div>
                                <h4 class="text-xl font-bold text-slate-900 mb-2">Nepalgunj Office</h4>
                                <p class="text-sm text-slate-500 leading-relaxed mb-6">Serves regional currency distribution, government account management, and bank inspection across mid-western districts.</p>
                                
                                <div class="space-y-3 text-sm text-slate-600 border-t border-slate-100 pt-5">
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Address</p>
                                            <p class="text-slate-600">Dhamboji, Nepalgunj, Banke</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Telephone</p>
                                            <p class="text-slate-600">+977-81-520241 / +977-81-520242</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Email</p>
                                            <p class="text-[#138496] font-medium">nepalgunj@nrb.org.np</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 6. Birendranagar -->
                        <div class="hub-card bg-white rounded-[20px] border border-slate-200 p-8 shadow-sm hover:border-[#1E3A5F]/20 transition-all flex flex-col justify-between">
                            <div>
                                <div class="flex items-center justify-between mb-4">
                                    <span class="inline-flex items-center rounded-full bg-slate-100 px-3.5 py-1 text-xs font-semibold text-[#25295B]">Karnali Province</span>
                                    <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md">Operational</span>
                                </div>
                                <h4 class="text-xl font-bold text-slate-900 mb-2">Birendranagar Office</h4>
                                <p class="text-sm text-slate-500 leading-relaxed mb-6">Manages currency availability, public access to financial services, and treasury operations for Karnali Province.</p>
                                
                                <div class="space-y-3 text-sm text-slate-600 border-t border-slate-100 pt-5">
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Address</p>
                                            <p class="text-slate-600">Airport Road, Birendranagar, Surkhet</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Telephone</p>
                                            <p class="text-slate-600">+977-83-520126 / +977-83-520127</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Email</p>
                                            <p class="text-[#138496] font-medium">surkhet@nrb.org.np</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 7. Dhangadhi -->
                        <div class="hub-card bg-white rounded-[20px] border border-slate-200 p-8 shadow-sm hover:border-[#1E3A5F]/20 transition-all flex flex-col justify-between col-span-2">
                            <div>
                                <div class="flex items-center justify-between mb-4">
                                    <span class="inline-flex items-center rounded-full bg-slate-100 px-3.5 py-1 text-xs font-semibold text-[#25295B]">Sudurpashchim Province</span>
                                    <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md">Operational</span>
                                </div>
                                <h4 class="text-xl font-bold text-slate-900 mb-2">Dhangadhi Office</h4>
                                <p class="text-sm text-slate-500 leading-relaxed mb-6">Extends central banking, currency chests, government accounting, and financial institution supervision across Sudurpashchim Province.</p>
                                
                                <div class="grid grid-cols-3 gap-6 text-sm text-slate-600 border-t border-slate-100 pt-5">
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"/><path d="M12 21.7C17.3 17 20 13 20 10a8 8 0 1 0-16 0c0 3 2.7 7 8 11.7z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Address</p>
                                            <p class="text-slate-600">Main Street, Dhangadhi, Kailali</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Telephone</p>
                                            <p class="text-slate-600">+977-91-522194 / +977-91-522195</p>
                                        </div>
                                    </div>
                                    <div class="flex items-start gap-3">
                                        <svg viewBox="0 0 24 24" class="h-5 w-5 text-[#138496] shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                                        <div>
                                            <p class="font-semibold text-slate-900">Email</p>
                                            <p class="text-[#138496] font-medium">dhangadhi@nrb.org.np</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

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
</body>

</html>'''

with open('pages/about/provincial-offices.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Redesigned provincial-offices.html successfully!")
