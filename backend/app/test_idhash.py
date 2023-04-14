from app.idhash import IdHash


class TestIdHash:
    def setup_method(self):
        self.idHash = IdHash()

    def test_hashLength(self):
        id = self.idHash.hash()
        assert len(id) == 12

    def test_hashIsUnique(self):
        id = self.idHash.hash()
        id2 = self.idHash.hash()
        assert id != id2
