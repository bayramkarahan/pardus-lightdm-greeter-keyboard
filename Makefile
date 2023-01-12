build:
	: run make install
install:
	mkdir -p $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/module
	mkdir -p $(DESTDIR)/usr/share/icons/hicolor/scalable/status/
	cp -prfv module/* $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/module/
	cp -pf icon/*.svg $(DESTDIR)/usr/share/icons/hicolor/scalable/status/
	#rm -rf $(DESTDIR)/usr/share/pardus/pardus-lightdm-greeter/data/icon
