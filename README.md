# 生成AIを用いたコードの自動変換

[English](./README_en.md)

このリポジトリでは、生成AIを用いてコードの言語を自動的に変換する機能を作成しています。

#### できること

- Python から C++ へ変換する

## 必要なライブラリ

- Python
  - バージョン 3.11.3 で動作確認済み
  - OpenAI または Anthropic または Ollama
  - Jupyter Notebook
  - networkx

### ライブラリインストール方法

Python環境において、以下を実行する。

```
pip install notebook
pip install openai
pip install anthropic
pip install ollama
pip install networkx
```

### GNU G++について

生成されたC++コードを確認するために、GNU G++を用いている。WindowsであればMinGWをインストールすることで使うことができる。
ターミナルで"g++"が使えることを事前に確認すること。

## 生成AIの利用について

このリポジトリでは、Open AI、Anthropic、OllamaのAPIを用いています。APIの詳細について、またAPI keyを有効化する方法については、それぞれのドキュメントをご参照ください。

## 使い方

「convert_code_language.ipynb」を開き、必要に応じて編集し、実行してください。

### 変換するPythonコードファイルの条件

- クラスの定義がされているファイルであること
- 一つのファイルの中にクラスは一つだけであること
- 外部のライブラリ（拡張モジュール）を利用していないこと
- PythonDependencyAnalyzerの引数に変換するPythonコードフォルダを指定する
- そのフォルダ内にPythonコードを格納していること

## サポート

新規にissueを作成して、詳細をお知らせください。

## 貢献

コミュニティからのプルリクエストを歓迎します。もし大幅な変更を考えているのであれば、提案する修正についての議論を始めるために、issueを開くことから始めてください。

また、プルリクエストを提出する際には、関連するテストが必要に応じて更新または追加されていることを確認してください。

## ライセンス

[MIT License](./LICENSE.txt)
