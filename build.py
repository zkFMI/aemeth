"""Build the bilingual, dependency-free æmeth site for GitHub Pages.

python3 build.py            -> public/  (English at /, Japanese at /ja/)
WORDMARK=Æmeth python3 build.py   -> same, with the capital ligature wordmark
"""
from pathlib import Path
from html import escape
import os
import shutil

ROOT = Path(__file__).parent
OUT = ROOT / 'public'
BASE = (os.environ.get('SITE_URL') or 'https://zkfmi.github.io/aemeth').rstrip('/')   # SITE_URL=https://aemeth.fi once the domain is live
WORDMARK = os.environ.get('WORDMARK', 'æmeth')          # 'æmeth' or 'Æmeth'
ZK = 'https://zkfmi.com/'
AETHEL = 'https://aethel.fi/'
GITHUB = 'https://github.com/zkFMI'
PLAUSIBLE = '''<!-- Privacy-friendly analytics by Plausible -->
<script async src="https://plausible.io/js/pa-wR0UNT6uwXVW4gCa_o6hy.js"></script>
<script>
  window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};
  plausible.init()
</script>'''
GLYPH_HERO = (ROOT / 'brand' / ('ae-upper-italic.path' if WORDMARK[0] == 'Æ' else 'ae-lower-italic.path')).read_text().strip()


def wm(cls=''):
    """The wordmark: the ligature is one span so it can be coloured and erased."""
    lig, rest = WORDMARK[0], WORDMARK[1:]
    uc = ' uc' if lig == 'Æ' else ''
    return f'<span class="wm{uc}{(" " + cls) if cls else ""}"><span class="ae">{lig}</span>{rest}</span>'


COPY = {
 'en': {
  'title': f'{WORDMARK} — financial infrastructure that settles what it cannot read',
  'description': f'{WORDMARK} develops zkFMI, a research stack for markets, clearing and settlement that act on proofs and commitments instead of reading the data, and Aethel, a payment-stream receivables application built on it.',
  'nav': [('build', 'What we build'), ('works', 'How it works'), ('evidence', 'Evidence'), ('name', 'The name'), ('pilot', 'Work with us')],
  'eyebrow': f'{WORDMARK} · developer of zkFMI · aemeth.fi',
  'h1': 'The state moves only while the proof holds.',
  'lede': f'{WORDMARK} builds financial market infrastructure in which the venue never sees the order, the settlement layer never sees the amount, and every state change is accepted only against a proof. The stack is zkFMI. The first application is Aethel.',
  'cta': 'How it works', 'cta2': 'Work with us',
  'hero_note': ['Research stack', 'Rust', 'MIT', 'No token', 'Custodies nothing'],
  'glyph_cap': f'{WORDMARK[0]} — the letter that has to stay',

  'build_eb': 'What we build',
  'build_h2': 'One stack. One application. Pilots with the people who would run it.',
  'build_p': f'Everything {WORDMARK} publishes is source, measured on stated hardware, with the limits written next to the numbers.',
  'cols': [
   ('Technology', 'zkFMI', 'A family of protocols: proof-carrying payment instructions, a settlement ledger of commitments, oblivious venues, anonymous eligibility and a decentralized central counterparty. Eight repositories, composed through explicit ports rather than shared state.', 'zkfmi.com', ZK, ''),
   ('Application', 'Aethel', 'Programmable payment-stream receivables. A signed payment stream becomes a receivable; independent credit assessors, guarantors, liquidity providers and servicers act on it with separately signed authority, and it settles through zkFMI.', 'aethel.fi', AETHEL, 'aleph'),
   ('Evaluation', 'Joint pilots', 'A concrete confidentiality problem, a scoped transaction path and acceptance criteria agreed in advance, with financial institutions, market operators and infrastructure teams, including the Avalanche ecosystem the ledger runs on.', 'What a pilot looks like', '#pilot', ''),
  ],

  'works_eb': 'How it works',
  'works_h2': 'Decide anywhere. Instruct once. Settle without reading.',
  'works_p': 'A value enters as a commitment and stays sealed through three layers. The market decides on it, the instruction carries it with its proofs, and the ledger moves it against those proofs. Nobody along the way opens it.',
  'flow': [
   ('01 · DECIDE', 'Venue', ['QOMM or OCLOB evaluate prices inside', 'multi-party computation. The best price', 'is proven minimal, never revealed.']),
   ('02 · INSTRUCT', 'zkPI', ['One typed instruction: range proofs,', 'nullifier, deadline, quorum signature.', 'Checkable by anyone, on any node.']),
   ('03 · SETTLE', 'DeFMI', ['A non-EVM Avalanche L1 verifies the', 'proofs and moves both legs together,', 'or neither.']),
  ],
  'flow_seal': 'C = commitment', 'flow_spine': 'the same commitment, never opened',
  'flow_note': 'Conceptual view. Which venue, proof path and trust assumptions apply depends on the deployment; the exact boundaries are in the wire specification and on the trust-boundary page.',
  'modules': [
   ('instruction', 'zkPI', 'Zero-knowledge payment instruction: what it commits to, what a venue checks, the wire layout and the verifier.', ZK + 'docs/zkpi.html', ''),
   ('ledger', 'DeFMI', 'A settlement layer that never reads the trade. Commitments on a non-EVM Avalanche L1; both legs move, or neither.', ZK + 'docs/defmi.html', ''),
   ('eligibility', 'DeKYX', 'Decentralized know-your-X. Prove only the qualification one action needs; the application never receives an identity record.', ZK + 'docs/dekyx.html', ''),
   ('clearing', 'DeCCP', 'Decentralized central counterparty. Threshold-governed clearing books, margin, confidential guarantee facilities, a deterministic loss waterfall.', ZK + 'docs/deccp.html', ''),
   ('venue · rfq', 'QOMM', 'Query-oblivious market making. A request for quote priced inside a seven-node MPC; the best quote is proved minimal and settled unopened.', ZK + 'docs/qomm.html', ''),
   ('venue · order book', 'OCLOB', 'Oblivious continuous limit order book. Side, price, size and identity stay hidden from the operator until matching is done.', ZK + 'docs/oclob.html', ''),
   ('build', 'Workflow DSL & SDK', 'Define who may change which rights, obligations and balances, run it on its own ledger, add settlement when the rails exist.', ZK + 'docs/build-applications.html', ''),
   ('application', 'Aethel', 'Payment-stream receivables: credit, guarantees, funding and servicing by independent providers, settled through zkPI and DeFMI.', AETHEL, 'app'),
  ],
  'works_a': 'Architecture', 'works_b': 'Source on GitHub',

  'ev_eb': 'Evidence, dated',
  'ev_h2': 'Working research. Numbers with an artifact behind them.',
  'ev_p': 'These are the headline measurements zkFMI publishes, on the hardware and at the widths stated there. They are reproduced here unchanged; the measurement page has the method and the run records.',
  'stats': [
   ('7.0 ms', 'to settle one DvP on 64-bit Bulletproof rails, one core'),
   ('3,424 B', 'settlement package on the wire at that width'),
   ('217 / s', 'settlements verified by one node on 8 workers'),
   ('96 B', 'proof that the ledger agrees with an external register, any size'),
   ('5 validators', 'non-EVM Avalanche L1, state roots agree across a restart'),
  ],
  'dated': 'as published on zkfmi.com · 2026-09-12',
  'bd_h3': 'What this is not',
  'bd_p': 'A research implementation. Not audited. It custodies nothing and there is no token. Every multi-node acceptance ran as processes or containers on one host under one administrator. No deployment has run across independent organisations, a real WAN, HSM-held keys or a legal finality regime.',
  'ev_a': 'Status: what is not production', 'ev_b': 'Measurements',

  'name_eb': 'The name',
  'name_h2': 'A letter that makes the thing move.',
  'quote': 'Write אמת, truth, on the clay and the golem walks. Erase the first letter and מת remains: dead.',
  'name_p': f'{WORDMARK} keeps that rule. A proof is the letter. While it holds, the state machine may move; take it away and nothing in the ledger changes, however much everyone else agrees. The spelling Aemeth is the historical one, from John Dee’s Sigillum Dei Aemeth; æ is the same word written as one letter.',
  'src': [('Golem legend, Jewish Museum Berlin', 'https://www.jmberlin.de/en/golem-from-mysticism-to-minecraft'), ('Sigillum Dei Aemeth, Sloane MS 3188', 'https://www.esotericarchives.com/dee/sl3188.htm')],
  'erase': 'Erase the letter', 'restore': 'Write it back',
  'state_on': 'proof holds · state may move', 'state_off': 'no proof · state frozen',

  'pilot_eb': 'Work with us',
  'pilot_h2': 'Bring a real workflow. Define what success means before we run it.',
  'pilot_p': 'We are looking for financial institutions, market operators and infrastructure teams who need to transact on shared infrastructure without exposing every input to it.',
  'steps': [
   ('Scope the problem', 'The transaction, the participants, and which inputs must stay confidential from whom.'),
   ('Agree the evaluation', 'Disclosure, correctness, integration with existing systems and failure recovery, written down as acceptance criteria.'),
   ('Run and inspect', 'Exercise the chosen path on zkFMI, inspect the artifacts, and record the gaps before any wider deployment.'),
  ],
  'who': 'There is no sales process and no form. The work is public: open an issue or a discussion on the zkFMI organisation, or start from the repositories.',
  'pilot_a': 'zkFMI on GitHub', 'pilot_b': 'Get started',

  'f_tag': f'{WORDMARK} (Aemeth) · developer of zkFMI',
  'f_note': f'{WORDMARK} is the project brand; zkFMI is the technology; Aethel is the receivables application. Research status and limits are stated on every page that makes a claim.',
  'skip': 'Skip to content', 'lang': '日本語', 'lang_href': 'ja/', 'lang_code': 'ja', 'navlabel': 'Main',
 },
 'ja': {
  'title': f'{WORDMARK} — 読まずに決済する金融市場インフラ',
  'description': f'{WORDMARK}（Aemeth）は、証明とコミットメントだけを根拠に市場・清算・決済が動く研究実装 zkFMI と、その上の支払ストリーム債権アプリケーション Aethel を開発しています。',
  'nav': [('build', 'つくっているもの'), ('works', '仕組み'), ('evidence', '実行記録'), ('name', '名前の由来'), ('pilot', '共同実証')],
  'eyebrow': f'{WORDMARK} · zkFMI の開発元 · aemeth.fi',
  'h1': '証明が成り立つ間だけ、状態が動く。',
  'lede': f'{WORDMARK}は、取引所が注文を見ず、決済層が金額を見ず、それでも状態の変化はすべて証明と引き換えにしか受け付けない金融市場インフラをつくっています。技術体系がzkFMI、最初のアプリケーションがAethelです。',
  'cta': '仕組みを見る', 'cta2': '共同実証について',
  'hero_note': ['研究実装', 'Rust', 'MIT', 'トークンなし', '資産を預からない'],
  'glyph_cap': f'{WORDMARK[0]} — 消してはいけない一文字',

  'build_eb': 'つくっているもの',
  'build_h2': '一つの技術体系。一つのアプリケーション。そして、実際に運用する人との実証。',
  'build_p': f'{WORDMARK}が公開するものはすべてソースコードで、明記した機材で計測し、数字の隣に限界を書いています。',
  'cols': [
   ('技術', 'zkFMI', '証明を伴う決済指図、コミットメントだけを載せる決済台帳、注文を見ない取引所、匿名の資格確認、分散型の清算機関からなるプロトコル群。8つのリポジトリを、状態の共有ではなく明示的なポートで組み合わせています。', 'zkfmi.com', ZK + 'ja/', ''),
   ('アプリケーション', 'Aethel', '支払ストリームをそのまま債権として扱う仕組み。署名済みの支払ストリームが債権になり、独立した与信・保証・資金供給・回収の事業者がそれぞれ署名した権限で関わり、zkFMIで決済します。', 'aethel.fi', AETHEL + 'ja/', 'aleph'),
   ('評価', '共同実証', '機密にしたい具体的な情報、範囲を絞った取引経路、先に合意した受入基準。金融機関・市場運営者・基盤チーム、そして台帳が載るAvalancheのエコシステムと一緒に進めます。', '実証の進め方', '#pilot', ''),
  ],

  'works_eb': '仕組み',
  'works_h2': 'どこで決めてもよい。指図は一度。決済は読まずに。',
  'works_p': '値はコミットメントとして入り、三つの層を封をしたまま通ります。市場はその上で判断し、指図は証明と一緒にそれを運び、台帳は証明と引き換えに動かします。途中で誰も開きません。',
  'flow': [
   ('01 · 決める', '取引所', ['QOMMやOCLOBが、秘密分散した入力の上で', '価格を評価。最良価格であることは', '明かさずに証明します。']),
   ('02 · 指図する', 'zkPI', ['型の決まった指図一つ。範囲証明、', 'nullifier、期限、閾値署名。', '誰でも、どのノードでも検証できます。']),
   ('03 · 決済する', 'DeFMI', ['非EVMのAvalanche L1が証明を検証し、', '両方の足を同時に動かすか、', 'どちらも動かさないかのどちらかです。']),
  ],
  'flow_seal': 'C = コミットメント', 'flow_spine': '同じコミットメント。一度も開かれない',
  'flow_note': '概念図です。どの取引所・証明経路・信頼前提が適用されるかは構成によります。正確な境界はwire仕様と信頼境界のページにあります。',
  'modules': [
   ('指図', 'zkPI', 'ゼロ知識証明付き決済指図。何をコミットし、市場が何を確かめ、wire上でどう並ぶか、検証器まで。', ZK + 'ja/docs/zkpi.html', ''),
   ('台帳', 'DeFMI', '取引の中身を読まない決済層。非EVMのAvalanche L1上のコミットメント。両方の足が動くか、どちらも動かないか。', ZK + 'ja/docs/defmi.html', ''),
   ('資格', 'DeKYX', '分散型 Know Your X。一つの行為に必要な資格だけを証明し、アプリケーションは本人情報を受け取らない。', ZK + 'ja/docs/dekyx.html', ''),
   ('清算', 'DeCCP', '分散型清算機関。閾値承認で統治する清算簿、証拠金、秘匿された保証枠、決定的な損失負担の順序。', ZK + 'ja/docs/deccp.html', ''),
   ('市場 · 見積', 'QOMM', '依頼を見ない見積市場。見積依頼を7ノードのMPCの中で値付けし、最良の見積を開かずに証明して決済。', ZK + 'ja/docs/qomm.html', ''),
   ('市場 · 指値板', 'OCLOB', '注文を見ない連続指値板。照合が終わるまで、売買の向き・価格・数量・参加者を運営者から隠す。', ZK + 'ja/docs/oclob.html', ''),
   ('構築', 'Workflow DSL & SDK', '誰がどの権利・義務・残高を変えてよいかを定義し、専用の台帳で動かし、レールが揃ったら決済を足す。', ZK + 'ja/docs/build-applications.html', ''),
   ('アプリケーション', 'Aethel', '支払ストリーム債権。与信・保証・資金供給・回収を独立した事業者が担い、zkPIとDeFMIで決済。', AETHEL + 'ja/', 'app'),
  ],
  'works_a': '全体構成', 'works_b': 'GitHubのソース',

  'ev_eb': '実行記録',
  'ev_h2': '動く研究実装。すべての数字に成果物がある。',
  'ev_p': 'zkFMIが公開している代表的な計測値を、そこに書かれた機材と幅のまま転記しています。計測方法と実行記録は計測ページにあります。',
  'stats': [
   ('7.0 ms', '64-bit Bulletproof、1コアでDvP一件を決済'),
   ('3,424 B', 'その幅での決済パッケージのwireサイズ'),
   ('217 / s', '1ノード8ワーカーで検証した決済件数'),
   ('96 B', '台帳と外部登録簿の一致を示す証明。規模によらず同じ長さ'),
   ('5 validators', '非EVM Avalanche L1。再起動をまたいで状態ルートが一致'),
  ],
  'dated': 'zkfmi.com の公開値 · 2026-09-12 時点',
  'bd_h3': 'これは何でないか',
  'bd_p': '研究実装であり、監査は未実施です。資産を預からず、トークンもありません。複数ノードでの受入試験はすべて、一人の管理者が管理する一台のホスト上のプロセスまたはコンテナで実行しました。独立した組織間、実際のWAN、HSMに置いた鍵、法的なファイナリティの下で動かした構成はまだありません。',
  'ev_a': '本番でないもの', 'ev_b': '計測値',

  'name_eb': '名前の由来',
  'name_h2': 'ものを動かす、一文字。',
  'quote': '粘土に אמת（真理）と書くとゴーレムは歩き出す。先頭の一文字を消すと מת（死）が残り、止まる。',
  'name_p': f'{WORDMARK}はこの規則をそのまま持ち込んでいます。証明がその一文字です。証明が成り立つ間だけ状態機械は動け、取り去れば、他の全員が同意していても台帳は変わりません。Aemethという綴りはジョン・ディーの Sigillum Dei Aemeth に見える歴史的なもので、æはその同じ語を一文字で書いた形です。',
  'src': [('ゴーレム伝説（ベルリン・ユダヤ博物館）', 'https://www.jmberlin.de/en/golem-from-mysticism-to-minecraft'), ('Sigillum Dei Aemeth, Sloane MS 3188', 'https://www.esotericarchives.com/dee/sl3188.htm')],
  'erase': '文字を消す', 'restore': '書き戻す',
  'state_on': '証明あり · 状態は動ける', 'state_off': '証明なし · 状態は止まる',

  'pilot_eb': '共同実証',
  'pilot_h2': '実際の業務を持ち込み、動かす前に「何をもって成功とするか」を決める。',
  'pilot_p': '共有の基盤で取引しながら、入力のすべてをその基盤に見せたくない金融機関・市場運営者・基盤チームを探しています。',
  'steps': [
   ('課題を絞る', '対象の取引、参加者、そして誰に対して何を秘匿すべきかを整理します。'),
   ('評価条件を決める', '開示範囲、正しさ、既存システムとの接続、障害からの復旧を、受入基準として書き出します。'),
   ('動かして確認する', '選んだ経路をzkFMIで実行し、成果物を確認し、展開前に埋まっていない点を記録します。'),
  ],
  'who': '営業窓口も入力フォームもありません。作業はすべて公開です。zkFMI organisationのissueかdiscussionを開くか、リポジトリから始めてください。',
  'pilot_a': 'GitHubのzkFMI', 'pilot_b': 'はじめかた',

  'f_tag': f'{WORDMARK}（Aemeth）· zkFMIの開発元',
  'f_note': f'{WORDMARK}はプロジェクトのブランド、zkFMIは技術、Aethelは債権アプリケーションです。研究段階であることと限界は、主張のあるページすべてに書いています。',
  'skip': '本文へ移動', 'lang': 'EN', 'lang_href': '../', 'lang_code': 'en', 'navlabel': 'メイン',
 },
}


def flow_svg(d):
    """Three stations, one sealed commitment passing over all of them."""
    xs = [0, 370, 740]
    W, BW, BH, Y = 1080, 340, 190, 96
    parts = [f'<svg viewBox="0 0 {W} {BH + Y + 10}" role="img" aria-label="{escape(d["works_h2"])}">']
    # seal at the left, spine across, lock at the right
    parts.append('<path class="seal" d="M4 40 l16 -22 h40 l16 22 l-16 22 h-40 z"/>')
    parts.append('<text class="cap" x="40" y="44" text-anchor="middle">C</text>')
    parts.append(f'<path class="spine" d="M84 40 H{W - 58}"/>')
    parts.append(f'<text class="cap" x="100" y="28">{escape(d["flow_seal"])}</text>')
    parts.append(f'<rect class="box" x="{W - 50}" y="22" width="50" height="36" rx="18"/>')
    parts.append(f'<path class="seal" d="M{W - 31} 39 v-6 a6 6 0 0 1 12 0 v6 M{W - 34} 39 h18 v10 h-18 z"/>')
    parts.append(f'<text class="cap" x="{W // 2}" y="72" text-anchor="middle">{escape(d["flow_spine"])}</text>')
    for i, (x, (lbl, ttl, lines)) in enumerate(zip(xs, d['flow'])):
        cx = x + BW // 2
        parts.append(f'<rect class="box" x="{x}" y="{Y}" width="{BW}" height="{BH}" rx="12"/>')
        parts.append(f'<path class="spine" d="M{cx} 40 V{Y}"/>')
        parts.append(f'<circle cx="{cx}" cy="40" r="5" fill="var(--night-aleph)"/>')
        parts.append(f'<text class="lbl" x="{x + 28}" y="{Y + 38}">{escape(lbl)}</text>')
        parts.append(f'<text class="ttl" x="{x + 28}" y="{Y + 74}">{escape(ttl)}</text>')
        for j, ln in enumerate(lines):
            parts.append(f'<text class="txt" x="{x + 28}" y="{Y + 108 + j * 22}">{escape(ln)}</text>')
        if i < 2:
            ax = x + BW
            parts.append(f'<path class="arrow" d="M{ax + 4} {Y + BH // 2} H{ax + 26} m-7 -6 l7 6 l-7 6"/>')
    parts.append('</svg>')
    return ''.join(parts)


def render(lang):
    d = COPY[lang]
    ja = lang == 'ja'
    p = '../' if ja else './'
    path = '/ja/' if ja else '/'
    nav = ''.join(f'<a href="#{k}">{escape(v)}</a>' for k, v in d['nav'])
    hero_note = ''.join(f'<span>{escape(s)}</span>' for s in d['hero_note'])
    cols = ''.join(
        f'<div class="col {cls}"><span class="kicker">{escape(k)}</span><h3>{escape(t)}</h3><p>{escape(b)}</p>'
        f'<a class="more" href="{href}">{escape(more)} <span class="arr">↗</span></a></div>'
        for k, t, b, more, href, cls in d['cols'])
    modules = ''.join(
        f'<a class="module {cls}" href="{href}"><span class="kicker">{escape(k)}</span><b>{escape(t)}</b><p>{escape(b)}</p></a>'
        for k, t, b, href, cls in d['modules'])
    stats = ''.join(f'<div class="stat"><b>{escape(n)}</b><span>{escape(s)}</span></div>' for n, s in d['stats'])
    steps = ''.join(f'<li><h3>{escape(t)}</h3><p>{escape(b)}</p></li>' for t, b in d['steps'])
    flow_list = ''.join(f'<li><span class="lbl">{escape(l)}</span><b>{escape(t)}</b><p>{escape(" ".join(ls))}</p></li>' for l, t, ls in d['flow'])
    src = ' · '.join(f'<a href="{href}">{escape(t)}</a>' for t, href in d['src'])
    zk = ZK + ('ja/' if ja else '')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(d['title'])}</title>
<meta name="description" content="{escape(d['description'])}">
<link rel="canonical" href="{BASE}{path}">
<link rel="alternate" hreflang="en" href="{BASE}/">
<link rel="alternate" hreflang="ja" href="{BASE}/ja/">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<meta property="og:title" content="{escape(d['title'])}">
<meta property="og:description" content="{escape(d['description'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:image" content="{BASE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f6f2ea">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{p}fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}style.css">
{PLAUSIBLE}
</head>
<body>
<a class="skip" href="#main">{escape(d['skip'])}</a>
<header class="top"><div class="wrap">
<a href="{p}" aria-label="{WORDMARK} home">{wm()}</a>
<nav aria-label="{escape(d['navlabel'])}">{nav}</nav>
<a class="lang" lang="{d['lang_code']}" hreflang="{d['lang_code']}" href="{d['lang_href']}">{escape(d['lang'])}</a>
</div></header>

<main id="main">
<section class="hero"><div class="wrap">
<div>
<p class="eyebrow">{escape(d['eyebrow'])}</p>
<h1>{escape(d['h1'])}</h1>
<p class="lede">{escape(d['lede'])}</p>
<div class="actions"><a class="btn primary" href="#works">{escape(d['cta'])} <span class="arr">↓</span></a><a class="btn" href="#pilot">{escape(d['cta2'])} <span class="arr">→</span></a></div>
<p class="hero-note">{hero_note}</p>
</div>
<figure class="glyph" aria-hidden="true"><svg viewBox="-10 -10 120 120"><circle class="ring" cx="50" cy="50" r="58"/><path d="{GLYPH_HERO}"/></svg><figcaption>{escape(d['glyph_cap'])}</figcaption></figure>
</div></section>

<section class="section" id="build"><div class="wrap">
<div class="head"><p class="eyebrow">{escape(d['build_eb'])}</p><div><h2>{escape(d['build_h2'])}</h2><p>{escape(d['build_p'])}</p></div></div>
<div class="cols">{cols}</div>
</div></section>

<section class="section night" id="works"><div class="wrap">
<div class="head"><p class="eyebrow">{escape(d['works_eb'])}</p><div><h2>{escape(d['works_h2'])}</h2><p>{escape(d['works_p'])}</p></div></div>
<div class="flow">{flow_svg(d)}</div>
<ol class="flow-list">{flow_list}</ol>
<p class="flow-note">{escape(d['flow_note'])}</p>
<div class="modules">{modules}</div>
<div class="actions"><a class="btn primary" href="{zk}docs/architecture.html">{escape(d['works_a'])} <span class="arr">↗</span></a><a class="btn" href="{GITHUB}">{escape(d['works_b'])} <span class="arr">↗</span></a></div>
</div></section>

<section class="section" id="evidence"><div class="wrap">
<div class="head"><p class="eyebrow">{escape(d['ev_eb'])}</p><div><h2>{escape(d['ev_h2'])}</h2><p>{escape(d['ev_p'])}</p></div></div>
<div class="stats">{stats}</div>
<p class="dated">{escape(d['dated'])}</p>
<div class="boundary"><h3>{escape(d['bd_h3'])}</h3><div><p>{escape(d['bd_p'])}</p>
<div class="actions"><a class="btn" href="{zk}docs/status.html">{escape(d['ev_a'])} <span class="arr">↗</span></a><a class="btn" href="{zk}docs/measurements.html">{escape(d['ev_b'])} <span class="arr">↗</span></a></div></div></div>
</div></section>

<section class="section paper-2" id="name"><div class="wrap">
<div class="head"><p class="eyebrow">{escape(d['name_eb'])}</p><div><h2>{escape(d['name_h2'])}</h2></div></div>
<div class="name">
<div class="name-demo" id="letter-demo">
{wm()}
<div class="hebrew" aria-hidden="true"><span class="ae">א</span>מת</div>
<div class="state"><span class="dot"></span><span class="state-text">{escape(d['state_on'])}</span></div>
<div><button type="button" aria-pressed="false" data-erase="{escape(d['erase'])}" data-restore="{escape(d['restore'])}" data-on="{escape(d['state_on'])}" data-off="{escape(d['state_off'])}">{escape(d['erase'])}</button></div>
</div>
<div><p class="quote">{escape(d['quote'])}</p><p>{escape(d['name_p'])}</p><p class="src">{src}</p></div>
</div>
</div></section>

<section class="section" id="pilot"><div class="wrap">
<div class="head"><p class="eyebrow">{escape(d['pilot_eb'])}</p><div><h2>{escape(d['pilot_h2'])}</h2><p>{escape(d['pilot_p'])}</p></div></div>
<ol class="steps">{steps}</ol>
<div class="who"><p>{escape(d['who'])}</p><div class="actions"><a class="btn primary" href="{GITHUB}">{escape(d['pilot_a'])} <span class="arr">↗</span></a><a class="btn" href="{zk}docs/get-started.html">{escape(d['pilot_b'])} <span class="arr">↗</span></a></div></div>
</div></section>
</main>

<footer><div class="wrap">
<div><a href="{p}" aria-label="{WORDMARK} home">{wm()}</a><p class="tag">{escape(d['f_tag'])}</p></div>
<p class="note">{escape(d['f_note'])}</p>
<div class="end"><span>© 2026 {WORDMARK}</span><a href="{zk}">zkfmi.com</a><a href="{AETHEL}{'ja/' if ja else ''}">aethel.fi</a><a href="{GITHUB}/aemeth">GitHub</a></div>
</div></footer>
<script src="{p}site.js" defer></script>
</body>
</html>
'''


def favicon():
    lig = (ROOT / 'brand' / ('ae-upper.path' if WORDMARK[0] == 'Æ' else 'ae-lower.path')).read_text().strip()
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#a1301f"/>'
            f'<g transform="translate(9 9) scale(0.46)"><path d="{lig}" fill="#f6f2ea"/></g></svg>')


if __name__ == '__main__':
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / 'ja').mkdir(parents=True)
    (OUT / 'index.html').write_text(render('en'))
    (OUT / 'ja' / 'index.html').write_text(render('ja'))
    shutil.copytree(ROOT / 'static', OUT, dirs_exist_ok=True)
    (OUT / 'favicon.svg').write_text(favicon())
    (OUT / '.nojekyll').touch()
    (OUT / 'version.txt').write_text(os.environ.get('GITHUB_SHA', 'local-preview') + '\n')
    (OUT / '404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found — æmeth</title><link rel="stylesheet" href="' + BASE + '/style.css">' + PLAUSIBLE + '<main class="wrap" style="padding:6rem 0"><h1>Page not found</h1><p><a class="btn" href="' + BASE + '/">Return to æmeth</a></p></main></html>')
    (OUT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + BASE + '/sitemap.xml\n')
    (OUT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join('<url><loc>' + BASE + q + '</loc></url>' for q in ('/', '/ja/')) + '</urlset>')
    print('Built æmeth (wordmark: %s) → public/' % WORDMARK)
