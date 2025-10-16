from stereo_vision_agri_robotics import info, __version__


def test_info_contains_version():
    d = info()
    assert d["version"] == __version__
    assert d["name"] == "stereo-vision-agri-robotics"
