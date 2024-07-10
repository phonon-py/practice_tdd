テスト駆動開発（TDD）を行う際のディレクトリ構造は、プロジェクトの規模や複雑さに応じて変わりますが、基本的なディレクトリ構造は以下のようになります。この例では、シンプルな電卓プロジェクトを想定しています。

### ディレクトリ構造

```
project_root/
├── calculator/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
└── requirements.txt
```

### 各ファイルの役割

- **project_root/**: プロジェクトのルートディレクトリです。
- **calculator/**: 電卓の機能を実装するためのパッケージディレクトリです。
  - **__init__.py**: このディレクトリをパッケージとして認識させるためのファイルです（空でも構いません）。
  - **calculator.py**: 電卓の機能を実装するモジュールです。
- **tests/**: テストコードを格納するディレクトリです。
  - **__init__.py**: このディレクトリをパッケージとして認識させるためのファイルです（空でも構いません）。
  - **test_calculator.py**: 電卓機能のテストケースを実装するモジュールです。
- **requirements.txt**: プロジェクトで必要なPythonパッケージを管理するファイルです（必要に応じて使用）。

### 各ファイルの内容

#### calculator/calculator.py

```python
def add(a, b):
    return a + b
```

#### tests/test_calculator.py

```python
import unittest
from calculator.calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

### テストの実行方法

プロジェクトのルートディレクトリに移動して、テストを実行します。

```bash
$ cd project_root
$ python -m unittest discover -s tests
```

このコマンドは `tests` ディレクトリ内のすべてのテストを自動的に検出して実行します。

### 追加の設定

- **requirements.txt**: プロジェクトで使用する依存関係がある場合、ここにリストします。例えば、`unittest` は標準ライブラリですが、他のサードパーティライブラリを使用する場合に記載します。

#### requirements.txt

```txt
# 必要に応じて依存関係を記載
```

この基本的なディレクトリ構造と設定を用いることで、プロジェクトの可読性とメンテナンス性を向上させることができます。