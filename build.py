"""Build the bilingual, dependency-free Aemeth site for GitHub Pages."""
from pathlib import Path
from html import escape
import os
import shutil

ROOT = Path(__file__).parent
OUT = ROOT / 'public'
BASE = (os.environ.get('SITE_URL') or 'https://zkfmi.github.io/aemeth').rstrip('/')
CONTACT = os.environ.get('CONTACT_URL', 'https://github.com/zkFMI')

COPY = {
    'en': {
        'title': 'æmeth — Confidential, verifiable financial infrastructure',
        'description': 'Aemeth develops zkFMI: financial infrastructure combining confidential computation and verifiable settlement. Explore the technology and discuss a joint pilot.',
        'nav': ['Approach', 'Technology', 'Evidence', 'Collaborate'],
        'eyebrow': 'AEMETH / FINANCIAL INFRASTRUCTURE',
        'headline': 'Keep the data private.<br>Make the outcome verifiable.',
        'intro': 'æmeth develops zkFMI — financial market infrastructure for institutions that need to transact together without exposing every input to the network.',
        'cta': 'Explore a joint pilot', 'secondary': 'Explore zkFMI',
        'hero_note': 'Confidential computation. Verifiable settlement. Built for evaluation with financial institutions.',
        'focus': 'OUR FOCUS', 'focus_title': 'Shared infrastructure.<br>Controlled disclosure.',
        'focus_body': 'Orders, pricing models and positions are commercially sensitive. Shared financial infrastructure must let participants verify the rules of a transaction while limiting who can see the underlying data.',
        'cases': [
            ('Confidential price discovery', 'Evaluate requests for quotes while protecting the customer’s request and the market maker’s pricing logic. Verify selection within the committed quote set.'),
            ('Delivery against payment', 'Link the asset and payment legs of a transaction. Verify the settlement conditions without publishing the underlying amounts and prices to validators.'),
            ('Collateral & settlement workflows', 'Explore workflows in which institutions need shared assurance over transfers and obligations, with disclosure defined for each participant and auditor.'),
        ],
        'tech_label': 'THE TECHNOLOGY', 'tech_title': 'zkFMI, developed by æmeth.',
        'tech_body': 'One technology stack connects confidential market decisions to verifiable state transitions. The technical specifications, source code and execution records remain open at zkfmi.com.',
        'flow': [('01 / COMPUTE', 'Private inputs', 'Multi-party computation evaluates a market operation over secret-shared inputs.'), ('02 / PROVE', 'Verifiable instruction', 'zkPI binds the settlement instruction to the applicable proof and authorization conditions.'), ('03 / SETTLE', 'Verified state', 'DeFMI validates the instruction and updates settlement state on a custom Avalanche L1.')],
        'flow_note': 'Conceptual flow. Disclosure and trust assumptions depend on the selected venue, proof path and deployment. See the technical documentation for exact boundaries.',
        'avalanche': 'Why Avalanche',
        'avalanche_body': 'DeFMI uses a custom, non-EVM Avalanche L1 with a Rust virtual machine. Proof verification and settlement rules are part of the chain’s state transition. This provides a concrete basis for evaluating confidential financial workflows with the Avalanche ecosystem.',
        'docs': 'Technical documentation', 'source': 'Source code',
        'evidence_label': 'CURRENT STAGE', 'evidence_title': 'Working research.<br>Inspectable evidence.',
        'evidence_body': 'The published research records document the path from market computation to native settlement. They also state the conditions under which those results were observed.',
        'observed': 'Documented execution', 'observed_body': 'Seven MPC processes and five AvalancheGo validators on a single host. Published runs cover confidential delivery against payment, consistent state roots and recovery checks; the scope varies by run.',
        'next': 'Next evaluation', 'next_body': 'Define a partner’s workflow and acceptance criteria, then evaluate the relevant path across deployment, disclosure, failure recovery and operational requirements.',
        'boundary': 'Research implementation. Single-host execution is not independent-operator deployment. Production readiness and third-party security validation remain open.',
        'evidence_link': 'Read implementation status & limitations', 'demo_link': 'Explore the demo paths',
        'collab_label': 'JOINT EVALUATION', 'collab_title': 'Bring a real workflow.<br>Define what success means.',
        'collab_body': 'We are looking for financial institutions, market operators and infrastructure teams to shape a focused pilot: a concrete confidentiality problem, a clearly scoped transaction path and measurable evaluation criteria.',
        'collab_steps': [('Scope the problem', 'Identify the transaction, participants and information that must remain confidential.'), ('Agree the evaluation', 'Define visibility, correctness, integration and recovery requirements together.'), ('Run & inspect', 'Exercise the chosen path, inspect results and record the gaps before wider deployment.')],
        'contact_title': 'Start a technical conversation', 'contact_body': 'Share the workflow you want to evaluate and the business and engineering teams who would take part.',
        'contact': 'Visit the project on GitHub',
        'brand_note': 'æmeth (Aemeth) is the project brand behind zkFMI. The name connects the idea of truth with systems whose state changes can be verified.',
        'footer': 'Confidentiality, with evidence.', 'skip': 'Skip to content',
    },
    'ja': {
        'title': 'æmeth — 機密性と検証可能性を両立する金融インフラ',
        'description': 'æmeth（Aemeth）は、秘匿計算と検証可能な決済をつなぐ金融市場インフラzkFMIを開発しています。金融事業者との共同実証に向けた技術と評価の入口。',
        'nav': ['取り組み', '技術', '実行記録', '共同実証'],
        'eyebrow': 'AEMETH / FINANCIAL INFRASTRUCTURE',
        'headline': 'データは秘匿する。<br>結果は検証できる。',
        'intro': 'æmethは、金融市場インフラ「zkFMI」を開発しています。取引の入力すべてをネットワークへ開示せずに、金融機関が共通の基盤で取引できる仕組みをつくります。',
        'cta': '共同実証について', 'secondary': 'zkFMIを知る',
        'hero_note': '秘匿計算と検証可能な決済をつなぎ、金融事業者との評価へ。',
        'focus': '取り組む課題', 'focus_title': '基盤を共有し、<br>開示を制御する。',
        'focus_body': '注文、価格決定モデル、保有ポジションは、事業上の機密情報です。金融インフラを共有するためには、入力情報を見られる範囲を限定しながら、取引がルールに沿っているかを検証できる必要があります。',
        'cases': [
            ('機密性を保つ価格探索', '顧客の見積依頼とマーケットメーカーの価格決定ロジックを保護しながら計算。コミットされた見積集合の範囲で、選択した価格を検証します。'),
            ('資産と代金の同時決済', '取引の資産移転と支払いを結び付け、金額や価格を検証者へ公開せずに決済条件を検証します。'),
            ('担保・決済業務の評価', '移転や債務の整合性を複数の金融機関で確認する業務を実証テーマとして検討。参加者と監査者ごとの開示範囲を定義します。'),
        ],
        'tech_label': '中核となる技術', 'tech_title': 'æmethが開発するzkFMI。',
        'tech_body': '秘匿された市場での判断から、検証可能な状態遷移までをつなぐ技術体系です。仕様・ソースコード・実行記録は、引き続きzkfmi.comから公開しています。',
        'flow': [('01 / COMPUTE', '入力を秘匿して計算', '秘密分散された入力に対して、マルチパーティ計算で市場の処理を実行します。'), ('02 / PROVE', '検証可能な決済指図', 'zkPIが、決済指図を適用する証明条件・認可条件に結び付けます。'), ('03 / SETTLE', '状態遷移を検証', 'DeFMIが指図を検証し、独自のAvalanche L1上で決済状態を更新します。')],
        'flow_note': '概念上の処理の流れです。開示範囲と信頼上の前提は、市場・証明経路・構成により異なります。正確な境界は技術資料をご覧ください。',
        'avalanche': 'Avalancheを使う理由',
        'avalanche_body': 'DeFMIはRust製の仮想マシンを持つ、非EVMの独自Avalanche L1です。証明の検証と決済ルールをチェーンの状態遷移に組み込み、Avalancheエコシステムで機密性を必要とする金融業務を評価する基盤にします。',
        'docs': '技術ドキュメント', 'source': 'ソースコード',
        'evidence_label': '現在の到達点', 'evidence_title': '動く研究実装。<br>確認できる実行記録。',
        'evidence_body': '市場での計算からネイティブ決済まで、公開した研究記録で確認できます。各記録には、その結果を観測した条件と限界を併記しています。',
        'observed': '記録された実行', 'observed_body': '単一ホスト上の7つのMPCプロセスと5つのAvalancheGo検証者。機密DvP決済、状態ルートの一致、復旧確認などを実行しており、確認範囲は各記録で示しています。',
        'next': '次に評価すること', 'next_body': '実証相手の業務と評価条件を定め、対象経路について構成・開示・障害復旧・運用要件を評価します。',
        'boundary': '現在は研究実装です。単一ホストでの実行は、独立した運営者による稼働を示すものではありません。本番運用への準備と第三者によるセキュリティ検証は今後の課題です。',
        'evidence_link': '実装状況と保証の範囲を読む', 'demo_link': 'デモの経路を知る',
        'collab_label': '共同実証', 'collab_title': '実際の業務から、<br>評価条件を一緒につくる。',
        'collab_body': '金融機関、市場運営者、金融インフラの開発チームとの実証を目指しています。機密性に関する具体的な課題を起点に、対象とする取引経路と測定可能な評価条件を絞り込みます。',
        'collab_steps': [('課題を絞る', '対象取引、参加者、機密にすべき情報を整理します。'), ('評価条件を決める', '情報の見え方、正確性、既存基盤との接続、復旧要件を合意します。'), ('動かして確認する', '対象経路を実行して結果を確認し、展開前の課題を記録します。')],
        'contact_title': '技術と業務の対話から', 'contact_body': '評価したい業務と、参加する業務・技術担当者についてお聞かせください。',
        'contact': 'GitHubのプロジェクトへ',
        'brand_note': 'æmeth（Aemeth）は、zkFMIを開発するプロジェクトのブランドです。「真理」という着想を、状態の変化を検証できるシステムに重ねています。',
        'footer': '機密性に、検証可能性を。', 'skip': '本文へ移動',
    }
}

def render(lang):
    d = COPY[lang]
    ja = lang == 'ja'
    prefix = '../' if ja else './'
    tech = 'https://zkfmi.com/' + ('ja/' if ja else '')
    path = '/ja/' if ja else '/'
    nav = ''.join(f'<a href="#{key}">{label}</a>' for key, label in zip(['approach','technology','evidence','collaborate'], d['nav']))
    cases = ''.join(f'<article class="case"><span class="number">0{i}</span><h3>{title}</h3><p>{body}</p></article>' for i,(title,body) in enumerate(d['cases'],1))
    flow = ''.join(f'<li><span class="eyebrow">{n}</span><h3>{title}</h3><p>{body}</p></li>' for n,title,body in d['flow'])
    steps = ''.join(f'<li><span class="number">0{i}</span><div><h3>{title}</h3><p>{body}</p></div></li>' for i,(title,body) in enumerate(d['collab_steps'],1))
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(d['title'])}</title><meta name="description" content="{escape(d['description'])}">
<link rel="canonical" href="{BASE}{path}"><link rel="alternate" hreflang="en" href="{BASE}/"><link rel="alternate" hreflang="ja" href="{BASE}/ja/"><link rel="alternate" hreflang="x-default" href="{BASE}/">
<meta property="og:title" content="{escape(d['title'])}"><meta property="og:description" content="{escape(d['description'])}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}{path}">
<meta name="theme-color" content="#1428db"><link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}style.css"></head>
<body><a class="skip" href="#main">{d['skip']}</a>
<header class="shell header"><a class="wordmark" aria-label="Aemeth home" href="{prefix}">æmeth<span class="wordmark-period">.</span></a><nav aria-label="{'メイン' if ja else 'Main'}">{nav}</nav><a class="language" lang="{'en' if ja else 'ja'}" hreflang="{'en' if ja else 'ja'}" href="{'../' if ja else './ja/'}">{'EN' if ja else '日本語'}</a></header>
<main id="main"><section class="shell hero"><p class="eyebrow">{d['eyebrow']}</p><h1>{d['headline']}</h1><p class="intro">{d['intro']}</p><div class="actions"><a class="button" href="#collaborate">{d['cta']} <span aria-hidden="true">↗</span></a><a class="text-link" href="{tech}">{d['secondary']} <span aria-hidden="true">↗</span></a></div><p class="hero-note">{d['hero_note']}</p></section>
<section class="section shell" id="approach"><div class="section-heading"><p class="eyebrow">{d['focus']}</p><div><h2>{d['focus_title']}</h2><p class="section-intro">{d['focus_body']}</p></div></div><div class="cases">{cases}</div></section>
<section class="technology" id="technology"><div class="shell"><div class="section-heading"><p class="eyebrow">{d['tech_label']}</p><div><h2>{d['tech_title']}</h2><p class="section-intro">{d['tech_body']}</p></div></div><ol class="flow">{flow}</ol><p class="caption">{d['flow_note']}</p><div class="avalanche"><h3>{d['avalanche']}</h3><p>{d['avalanche_body']}</p></div><div class="actions"><a class="button light" href="{tech}docs/">{d['docs']} <span aria-hidden="true">↗</span></a><a class="text-link" href="https://github.com/zkFMI">{d['source']} <span aria-hidden="true">↗</span></a></div></div></section>
<section class="section shell" id="evidence"><div class="section-heading"><p class="eyebrow">{d['evidence_label']}</p><div><h2>{d['evidence_title']}</h2><p class="section-intro">{d['evidence_body']}</p></div></div><div class="evidence-grid"><article><p class="eyebrow">RESEARCH EXECUTION</p><h3>{d['observed']}</h3><p>{d['observed_body']}</p></article><article><p class="eyebrow">PARTNER EVALUATION</p><h3>{d['next']}</h3><p>{d['next_body']}</p></article></div><p class="boundary">{d['boundary']}</p><div class="actions"><a class="text-link" href="{tech}docs/status.html">{d['evidence_link']} <span aria-hidden="true">↗</span></a><a class="text-link" href="{tech}docs/optimistic.html">{d['demo_link']} <span aria-hidden="true">↗</span></a></div></section>
<section class="collaborate" id="collaborate"><div class="shell"><div class="section-heading"><p class="eyebrow">{d['collab_label']}</p><div><h2>{d['collab_title']}</h2><p class="section-intro">{d['collab_body']}</p></div></div><ol class="steps">{steps}</ol><div class="contact"><div><h3>{d['contact_title']}</h3><p>{d['contact_body']}</p></div><a class="button" href="{escape(CONTACT, quote=True)}">{d['contact']} <span aria-hidden="true">↗</span></a></div></div></section>
</main><footer class="shell footer"><div><a class="wordmark" aria-label="Aemeth home" href="{prefix}">æmeth<span class="wordmark-period">.</span></a><p>{d['footer']}</p></div><p class="brand-note">{d['brand_note']}</p><div class="footer-end"><span>© 2026 Aemeth</span><a href="{tech}">zkfmi.com</a><a href="https://aethel.fi/">Aethel</a><a href="https://github.com/zkFMI/aemeth">GitHub</a></div></footer></body></html>'''

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    (OUT/'ja').mkdir(exist_ok=True)
    (OUT/'index.html').write_text(render('en'))
    (OUT/'ja/index.html').write_text(render('ja'))
    for name in ('style.css','favicon.svg'):
        shutil.copyfile(ROOT/'static'/name, OUT/name)
    (OUT/'.nojekyll').touch()
    (OUT/'404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found — Aemeth</title><main><h1>Page not found</h1><p><a href="'+BASE+'/">Return to Aemeth</a></p></main></html>')
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\n')
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+BASE+p+'</loc></url>' for p in ('/','/ja/'))+'</urlset>')
    revision = os.environ.get('GITHUB_SHA', 'local-preview')
    (OUT/'version.txt').write_text(revision+'\n')
    print('Built English and Japanese pages in public/')
