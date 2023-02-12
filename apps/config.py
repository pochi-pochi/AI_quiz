from pathlib import Path

basedir = Path(__file__).parent.parent


# BaseConfigクラス
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"


# BaseConfigを継承したLocalConfigクラス
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# BaseConfigを継承したTestConfigクラス
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


# config辞書にマッピングする
config = {
    "testing": TestConfig,
    "local": LocalConfig,
}


# クイズのお題の一覧
QUIZ = [
    "Python",
    "C",
    "C++",
    "クラウド",
    "プログラム",
    "AI",
    "エディター",
    "データサイエンス",
    "OS",
    "競技プログラミング",
    "エッジAI",
    "PC",
    "フロントエンド",
    "バックエンド",
    "ラズパイ",
    "Jetson",
    "フレームワーク",
    "メモリ",
    "CSRF",
    "ルーター",
]
