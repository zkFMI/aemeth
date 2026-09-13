# 発注: aemeth.fi の DNS を GitHub Pages へ向ける（Marcaria）

## 背景
- aemeth.fi は Marcaria で登録完了済み（NS: ns01-03.trademarkarea.com）。
- 現在の A レコードは Marcaria の仮ページ（199.83.135.102 / 192.230.79.89、Incapsula）。
- GitHub 側は設定済み: リポジトリ zkFMI/aemeth の Pages カスタムドメインに aemeth.fi を登録済み。
- 2026-09-13 に同じアカウントで aethel.fi を同じ手順で設定した実績がある（apex A ×4 + www CNAME）。

## やること（これだけ）
1. ユーザーが普段使う Chrome（ログイン済みのはず）で https://www.marcaria.com/ のアカウント画面を開く。
   - **ログインしていなければ、そこで止めて報告する。メールアドレス・パスワードは絶対に入力しない。**
2. ドメイン一覧から aemeth.fi の DNS 管理（DNS Records / Zone）を開く。
3. apex（@ / aemeth.fi）の既存 A レコード（Marcaria 仮ページ向け 199.83.135.102、192.230.79.89 など）を削除し、次を保存する。
   | 名前 | 種別 | 値 |
   | --- | --- | --- |
   | @ | A | 185.199.108.153 |
   | @ | A | 185.199.109.153 |
   | @ | A | 185.199.110.153 |
   | @ | A | 185.199.111.153 |
   | www | CNAME | zkfmi.github.io |
   - www に既存の A / CNAME（incapdns 向け）があれば削除して CNAME に置き換える。
   - MX / TXT など他のレコードは触らない。
   - URL 転送（web forwarding）や Marcaria のパーキング設定が有効なら無効化する。
4. 保存後、保存された一覧のスクリーンショットを
   `/private/tmp/claude-501/-Users-shukob-Research-DeFMI/09dce8af-dbd9-4144-94f4-175c0e6a739d/scratchpad/marcaria-aemeth-dns.png`
   に保存する。
5. ターミナルで `dig +short A aemeth.fi` と `dig +short CNAME www.aemeth.fi` を実行し、結果をそのまま報告する（反映前でもよい。反映待ちならそう書く）。

## やらないこと
- aethel.fi や他のドメインの設定に触らない。
- ドメインの購入・更新・その他の購買操作をしない。
- GitHub 側（Pages 設定、リポジトリ、変数）には触らない。こちらで済んでいる。
- ファイルの編集・git 操作をしない。
- 認証情報の入力をしない（ログインが必要ならユーザーに依頼して止まる）。

## 報告の形式
- ログイン状態（済 / 未）
- 削除したレコード、追加したレコード（保存後の一覧の転記）
- スクリーンショットのパス
- dig の出力
- できなかったことがあればその理由
