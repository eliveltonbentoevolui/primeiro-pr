from saudacao import saudacao


def test_saudacao_inclui_nome():
    assert "Ola, mundo!" in saudacao("mundo")


def test_saudacao_menciona_pr():
    assert "primeiro PR" in saudacao("mundo")
