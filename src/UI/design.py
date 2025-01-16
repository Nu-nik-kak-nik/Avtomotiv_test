# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_SystemPulse(object):
    def setupUi(self, SystemPulse):
        if not SystemPulse.objectName():
            SystemPulse.setObjectName(u"SystemPulse")
        SystemPulse.resize(671, 492)
        SystemPulse.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setItalic(False)
        SystemPulse.setFont(font)
        SystemPulse.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        SystemPulse.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0439 \u0444\u043e\u043d \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f */\n"
"QWidget {\n"
"    background-color: #1A1A1A;\n"
"    color: #ffffff;\n"
"    font-family: \"Arial\";\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0432\u043a\u043b\u0430\u0434\u043e\u043a */\n"
"QTabWidget {\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 \u0432\u043a\u043b\u0430\u0434\u043e\u043a */\n"
"QTabBar::tab {\n"
"    background-color: #222222; \n"
"    color: #ffffff;          \n"
"    padding: 8px 16px;      \n"
"    border-top-left-radius: 5px;    \n"
"    border-top-right-radius: 5px;  \n"
"    margin-right: 2px; \n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 \u0432\u043a\u043b\u0430\u0434\u043a\u0438 */\n"
"QTabBar::tab:selected {\n"
"    backgr"
                        "ound-color: #342882; \n"
"    color: #ffffff;\n"
"    border-bottom: 2px solid #342882; \n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 \u0432\u043a\u043b\u0430\u0434\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QTabBar::tab:hover {\n"
"    background-color: #2C226D;  \n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"QPushButton {\n"
"    background-color: #342882;\n"
"    color: #ffffff;\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"QPushButton:hover {\n"
"    background-color: #2C226D;; \n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430"
                        "\u0446\u0438\u044f \u043a\u043d\u043e\u043f\u043e\u043a \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QPushButton:pressed {\n"
"    background-color: #222222; \n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0433\u0440\u0435\u0441\u0441 \u0431\u0430\u0440\u0430 */\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    background-color: #222222;\n"
"    text-align: center;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #342882;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f QSpinBox */\n"
"QSpinBox {\n"
"    background-color: #222222; \n"
"    color: #ffffff;          \n"
"    border-radius: 3px; \n"
"}\n"
"\n"
"QSpinBox:hover{\n"
"  background-color: #222229; \n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: right;\n"
"	background-color: #342882; \n"
"	border-radius: 3px; \n"
"}\n"
"QSpin"
                        "Box::down-button {\n"
"	subcontrol-origin: border;\n"
"    subcontrol-position: left;\n"
"	background-color: #342882; \n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"QTableView, QTableWidget {\n"
"    border-radius: 5px;\n"
"    background-color: #222222;\n"
"    gridline-color: #333333;\n"
"    selection-background-color: #342882;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2A2A2A;\n"
"    color: #ffffff; \n"
"    padding: 5px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border: 1px solid #222222;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    border: 1px solid #333333;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #342882;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    border: none; \n"
"}\n"
"\n"
"QHeaderView::section:horizontal:hover {\n"
"    background-color: #2A2A2A; \n"
"}\n"
""
                        "\n"
"QScrollBar:vertical {\n"
"    width: 14px;\n"
"    background-color: #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #342882;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 14px;\n"
"    background-color: #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #342882;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0438\u0436\u043d\u0438\u0445 \u043a\u043d\u043e\u043f\u043e\u043a \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: #333333;\n"
"    border: none;\n"
"    height: 14px;\n"
"	width: 14px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: #444444; \n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background-"
                        "color: #222222;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal:hover,\n"
"QScrollBar::sub-page:horizontal:hover {\n"
"	 background-color: #2A2A2A;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0431\u043e\u043a\u043e\u0432\u044b\u0445 \u043a\u043d\u043e\u043f\u043e\u043a \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: #333333; \n"
"    border: none;\n"
"    width: 14px;\n"
"    height: 14px; \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover,\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: #444444; \n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: #222222; \n"
"    border: none;\n"
"}\n"
"QScrollBar::add-page:vertical:hover,\n"
"QScrollBar::sub-page:vertical:hover {\n"
"     background-color: #2A2A2A;\n"
"}")
        SystemPulse.setDockNestingEnabled(False)
        self.centralwidget = QWidget(SystemPulse)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_SystemPulse = QTabWidget(self.centralwidget)
        self.tabWidget_SystemPulse.setObjectName(u"tabWidget_SystemPulse")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.tabWidget_SystemPulse.setFont(font1)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labe_CPU = QLabel(self.tab_3)
        self.labe_CPU.setObjectName(u"labe_CPU")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        self.labe_CPU.setFont(font2)
        self.labe_CPU.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labe_CPU, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 2, 1, 1)

        self.label_RAM = QLabel(self.tab_3)
        self.label_RAM.setObjectName(u"label_RAM")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_RAM.sizePolicy().hasHeightForWidth())
        self.label_RAM.setSizePolicy(sizePolicy)
        self.label_RAM.setFont(font2)
        self.label_RAM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_RAM, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_play = QPushButton(self.tab_3)
        self.pushButton_play.setObjectName(u"pushButton_play")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy1)
        self.pushButton_play.setMinimumSize(QSize(0, 38))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(False)
        self.pushButton_play.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_play)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout, 10, 0, 1, 5)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.progressBar_CPU = QProgressBar(self.tab_3)
        self.progressBar_CPU.setObjectName(u"progressBar_CPU")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar_CPU.sizePolicy().hasHeightForWidth())
        self.progressBar_CPU.setSizePolicy(sizePolicy2)
        self.progressBar_CPU.setMinimumSize(QSize(0, 36))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(15)
        font4.setItalic(False)
        self.progressBar_CPU.setFont(font4)
        self.progressBar_CPU.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.progressBar_CPU.setValue(0)

        self.gridLayout.addWidget(self.progressBar_CPU, 3, 2, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.label_interval = QLabel(self.tab_3)
        self.label_interval.setObjectName(u"label_interval")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(15)
        self.label_interval.setFont(font5)

        self.horizontalLayout_4.addWidget(self.label_interval)

        self.horizontalSpacer_14 = QSpacerItem(15, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.spinBox_update_interval = QSpinBox(self.tab_3)
        self.spinBox_update_interval.setObjectName(u"spinBox_update_interval")
        self.spinBox_update_interval.setMinimumSize(QSize(60, 0))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(16)
        self.spinBox_update_interval.setFont(font6)
        self.spinBox_update_interval.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.spinBox_update_interval.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox_update_interval.setMinimum(1)
        self.spinBox_update_interval.setMaximum(60)
        self.spinBox_update_interval.setValue(1)

        self.horizontalLayout_4.addWidget(self.spinBox_update_interval)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_13)


        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 0, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.label_ROM = QLabel(self.tab_3)
        self.label_ROM.setObjectName(u"label_ROM")
        sizePolicy.setHeightForWidth(self.label_ROM.sizePolicy().hasHeightForWidth())
        self.label_ROM.setSizePolicy(sizePolicy)
        self.label_ROM.setFont(font2)
        self.label_ROM.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_ROM, 5, 0, 1, 1)

        self.horizontalLayout_ROM = QHBoxLayout()
        self.horizontalLayout_ROM.setSpacing(0)
        self.horizontalLayout_ROM.setObjectName(u"horizontalLayout_ROM")
        self.horizontalLayout_ROM.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_ROM_free = QLabel(self.tab_3)
        self.label_ROM_free.setObjectName(u"label_ROM_free")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_ROM_free.sizePolicy().hasHeightForWidth())
        self.label_ROM_free.setSizePolicy(sizePolicy3)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setItalic(False)
        self.label_ROM_free.setFont(font7)
        self.label_ROM_free.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label_ROM_free.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_ROM.addWidget(self.label_ROM_free)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(16)
        font8.setItalic(False)
        self.label_2.setFont(font8)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_ROM.addWidget(self.label_2)

        self.label_ROM_all = QLabel(self.tab_3)
        self.label_ROM_all.setObjectName(u"label_ROM_all")
        sizePolicy3.setHeightForWidth(self.label_ROM_all.sizePolicy().hasHeightForWidth())
        self.label_ROM_all.setSizePolicy(sizePolicy3)
        self.label_ROM_all.setFont(font7)
        self.label_ROM_all.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label_ROM_all.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_ROM.addWidget(self.label_ROM_all)


        self.gridLayout.addLayout(self.horizontalLayout_ROM, 5, 3, 1, 1)

        self.horizontalLayout_RAM = QHBoxLayout()
        self.horizontalLayout_RAM.setSpacing(0)
        self.horizontalLayout_RAM.setObjectName(u"horizontalLayout_RAM")
        self.horizontalLayout_RAM.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_RAM_free = QLabel(self.tab_3)
        self.label_RAM_free.setObjectName(u"label_RAM_free")
        sizePolicy3.setHeightForWidth(self.label_RAM_free.sizePolicy().hasHeightForWidth())
        self.label_RAM_free.setSizePolicy(sizePolicy3)
        self.label_RAM_free.setFont(font7)
        self.label_RAM_free.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label_RAM_free.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_RAM.addWidget(self.label_RAM_free)

        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setFont(font8)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_RAM.addWidget(self.label)

        self.label_RAM_all = QLabel(self.tab_3)
        self.label_RAM_all.setObjectName(u"label_RAM_all")
        sizePolicy3.setHeightForWidth(self.label_RAM_all.sizePolicy().hasHeightForWidth())
        self.label_RAM_all.setSizePolicy(sizePolicy3)
        self.label_RAM_all.setMaximumSize(QSize(16777215, 16777215))
        self.label_RAM_all.setFont(font7)
        self.label_RAM_all.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label_RAM_all.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_RAM.addWidget(self.label_RAM_all)


        self.gridLayout.addLayout(self.horizontalLayout_RAM, 4, 3, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_load = QLabel(self.tab_3)
        self.label_load.setObjectName(u"label_load")
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(18)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setUnderline(False)
        font9.setStrikeOut(False)
        self.label_load.setFont(font9)
        self.label_load.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_load)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 5)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 5, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 9, 0, 1, 1)

        self.label_time = QLabel(self.tab_3)
        self.label_time.setObjectName(u"label_time")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy5)
        self.label_time.setFont(font4)
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_time, 11, 0, 1, 5)

        self.tabWidget_SystemPulse.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_2 = QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_DB = QLabel(self.tab_4)
        self.label_DB.setObjectName(u"label_DB")
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(18)
        font10.setBold(True)
        self.label_DB.setFont(font10)

        self.horizontalLayout_2.addWidget(self.label_DB)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.pushButton_remove = QPushButton(self.tab_4)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(15)
        font11.setBold(True)
        self.pushButton_remove.setFont(font11)

        self.horizontalLayout_2.addWidget(self.pushButton_remove)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tableWidget_DB = QTableWidget(self.tab_4)
        if (self.tableWidget_DB.columnCount() < 9):
            self.tableWidget_DB.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_DB.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_DB.setObjectName(u"tableWidget_DB")
        self.tableWidget_DB.setFont(font1)

        self.verticalLayout_2.addWidget(self.tableWidget_DB)

        self.tabWidget_SystemPulse.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget_SystemPulse)

        SystemPulse.setCentralWidget(self.centralwidget)

        self.retranslateUi(SystemPulse)

        self.tabWidget_SystemPulse.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SystemPulse)
    # setupUi

    def retranslateUi(self, SystemPulse):
        SystemPulse.setWindowTitle(QCoreApplication.translate("SystemPulse", u"SystemPulse", None))
#if QT_CONFIG(tooltip)
        self.labe_CPU.setToolTip(QCoreApplication.translate("SystemPulse", u"\u041d\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u043d\u0430 \u0426\u041f \u0432 %", None))
#endif // QT_CONFIG(tooltip)
        self.labe_CPU.setText(QCoreApplication.translate("SystemPulse", u"\u0426\u041f:", None))
#if QT_CONFIG(tooltip)
        self.label_RAM.setToolTip(QCoreApplication.translate("SystemPulse", u"\u041e\u0417\u0423 \u0441\u0432\u043e\u0434\u043d\u043e/\u0432\u0441\u0435\u0433\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.label_RAM.setText(QCoreApplication.translate("SystemPulse", u"\u041e\u0417\u0423:", None))
        self.pushButton_play.setText(QCoreApplication.translate("SystemPulse", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.label_interval.setText(QCoreApplication.translate("SystemPulse", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f (\u0441\u0435\u043a):", None))
#if QT_CONFIG(tooltip)
        self.label_ROM.setToolTip(QCoreApplication.translate("SystemPulse", u"\u041f\u0417\u0423 \u0441\u0432\u043e\u0434\u043d\u043e/\u0432\u0441\u0435\u0433\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.label_ROM.setText(QCoreApplication.translate("SystemPulse", u"\u041f\u0417\u0423:", None))
#if QT_CONFIG(tooltip)
        self.label_ROM_free.setToolTip(QCoreApplication.translate("SystemPulse", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.label_ROM_free.setText(QCoreApplication.translate("SystemPulse", u"0", None))
        self.label_2.setText(QCoreApplication.translate("SystemPulse", u" / ", None))
#if QT_CONFIG(tooltip)
        self.label_ROM_all.setToolTip(QCoreApplication.translate("SystemPulse", u"\u0412\u0441\u0435\u0433\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.label_ROM_all.setText(QCoreApplication.translate("SystemPulse", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_RAM_free.setToolTip(QCoreApplication.translate("SystemPulse", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.label_RAM_free.setText(QCoreApplication.translate("SystemPulse", u"0", None))
        self.label.setText(QCoreApplication.translate("SystemPulse", u" / ", None))
#if QT_CONFIG(tooltip)
        self.label_RAM_all.setToolTip(QCoreApplication.translate("SystemPulse", u"\u0412\u0441\u0435\u0433\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.label_RAM_all.setText(QCoreApplication.translate("SystemPulse", u"0", None))
        self.label_load.setText(QCoreApplication.translate("SystemPulse", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u0438:", None))
        self.label_time.setText("")
        self.tabWidget_SystemPulse.setTabText(self.tabWidget_SystemPulse.indexOf(self.tab_3), QCoreApplication.translate("SystemPulse", u"\u041c\u043e\u043d\u0438\u0442\u043e\u0440\u0438\u043d\u0433", None))
        self.label_DB.setText(QCoreApplication.translate("SystemPulse", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u0411\u0414:", None))
        self.pushButton_remove.setText(QCoreApplication.translate("SystemPulse", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        ___qtablewidgetitem = self.tableWidget_DB.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SystemPulse", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_DB.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SystemPulse", u"\u0418\u043d\u0442\u0435\u0440\u0432\u0430\u043b (\u0441\u0435\u043a)", None));
        ___qtablewidgetitem2 = self.tableWidget_DB.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SystemPulse", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem3 = self.tableWidget_DB.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SystemPulse", u"\u0412\u0440\u0435\u043c\u044f", None));
        ___qtablewidgetitem4 = self.tableWidget_DB.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SystemPulse", u"\u0426\u041f (%)", None));
        ___qtablewidgetitem5 = self.tableWidget_DB.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SystemPulse", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e \u041e\u0417\u0423 (\u041c\u0431)", None));
        ___qtablewidgetitem6 = self.tableWidget_DB.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SystemPulse", u"\u0412\u0441\u0435\u0433\u043e \u041e\u0417\u0423 (\u041c\u0431)", None));
        ___qtablewidgetitem7 = self.tableWidget_DB.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SystemPulse", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u043e \u041f\u0417\u0423 (\u0413\u0431)", None));
        ___qtablewidgetitem8 = self.tableWidget_DB.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SystemPulse", u"\u0412\u0441\u0435\u0433\u043e \u041f\u0417\u0423 (\u0413\u0431)", None));
        self.tabWidget_SystemPulse.setTabText(self.tabWidget_SystemPulse.indexOf(self.tab_4), QCoreApplication.translate("SystemPulse", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
    # retranslateUi

