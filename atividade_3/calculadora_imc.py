# -*- coding: latin1 -*-
import wx


class CalculadoraImc(wx.Frame):
    def __init__(self):
        super().__init__(parent=None)
        self.lbl_resultado_imc = None
        self.lbl_classe_imc = None
        self.input_nome = None
        self.input_endereco = None
        self.input_altura = None
        self.input_peso = None
        self.init_ui()

    def init_ui(self):
        window = wx.Panel(self)
        box_vertical = wx.BoxSizer(wx.VERTICAL)

        # Nome
        box_nome = wx.BoxSizer(wx.HORIZONTAL)
        lbl_nome = wx.StaticText(window, label="Nome:")
        box_nome.Add(lbl_nome, flag=wx.RIGHT, border=8)
        self.input_nome = wx.TextCtrl(window)
        box_nome.Add(self.input_nome, proportion=1)
        box_vertical.Add(box_nome, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Endereço
        box_endereco = wx.BoxSizer(wx.HORIZONTAL)
        lbl_endereco = wx.StaticText(window, label="Endereço:")
        box_endereco.Add(lbl_endereco, flag=wx.RIGHT, border=8)
        self.input_endereco = wx.TextCtrl(window)
        box_endereco.Add(self.input_endereco, proportion=1)
        box_vertical.Add(box_endereco, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Altura
        box_altura = wx.BoxSizer(wx.HORIZONTAL)
        lbl_altura = wx.StaticText(window, label="Altura (cm):")
        box_altura.Add(lbl_altura, flag=wx.RIGHT, border=8)
        self.input_altura = wx.TextCtrl(window)
        box_altura.Add(self.input_altura, proportion=1)
        box_vertical.Add(box_altura, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Peso
        box_peso = wx.BoxSizer(wx.HORIZONTAL)
        lbl_peso = wx.StaticText(window, label="Peso (kg):")
        box_peso.Add(lbl_peso, flag=wx.RIGHT, border=8)
        self.input_peso = wx.TextCtrl(window)
        box_peso.Add(self.input_peso, proportion=1)
        box_vertical.Add(box_peso, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Resultado
        box_resultado = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl_resultado_imc = wx.StaticText(window, label="")
        self.lbl_classe_imc = wx.StaticText(window, label="")
        box_resultado.Add(self.lbl_resultado_imc, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        box_resultado.Add(self.lbl_classe_imc, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        box_vertical.Add(box_resultado, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        # Botões
        box_botoes = wx.BoxSizer(wx.HORIZONTAL)

        btn_calculate = wx.Button(window, label="Calcular IMC")
        btn_calculate.Bind(wx.EVT_BUTTON, self.calcular_imc)
        box_botoes.Add(btn_calculate,  proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        btn_reset = wx.Button(window, label="Reiniciar")
        btn_reset.Bind(wx.EVT_BUTTON, self.reset)
        box_botoes.Add(btn_reset, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        btn_fechar = wx.Button(window, label="Sair")
        btn_fechar.Bind(wx.EVT_BUTTON, self.fechar)
        box_botoes.Add(btn_fechar, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        box_vertical.Add(box_botoes, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        window.SetSizer(box_vertical)

        self.SetTitle("Cálculo do IMC - Índice de Massa Corporal")
        self.SetSize(500, 250)
        self.Centre()

    def calcular_imc(self, event):
        try:
            altura = float(self.input_altura.GetValue()) / 100
            peso = float(self.input_peso.GetValue())
            imc = peso / (altura ** 2)
            classe_imc = self.classificar_imc(imc)
            self.lbl_resultado_imc.SetLabel(f"IMC: {imc:.2f}")
            self.lbl_classe_imc.SetLabel(f"Classificação: {classe_imc}")
        except ValueError:
            wx.MessageBox("Insira valores válidos para peso e altura.", "Erro", wx.OK | wx.ICON_ERROR)

    def reset(self, event):
        self.input_nome.SetValue("")
        self.input_endereco.SetValue("")
        self.input_peso.SetValue("")
        self.input_altura.SetValue("")
        self.lbl_resultado_imc.SetLabel("")
        self.lbl_classe_imc.SetLabel("")

    def fechar(self, event):
        self.Close()

    @staticmethod
    def classificar_imc(imc):
        if imc < 17:
            return "Muito abaixo do peso"
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade I"
        elif 35 <= imc < 39.9:
            return "Obesidade II (severa)"
        else:
            return "Obesidade III (mórbida)"


if __name__ == "__main__":
    app = wx.App()
    frame = CalculadoraImc()
    frame.Show()
    app.MainLoop()
