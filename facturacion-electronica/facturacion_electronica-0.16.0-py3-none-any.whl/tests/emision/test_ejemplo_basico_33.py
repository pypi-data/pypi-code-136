# -#- coding: utf-8 -#-
from facturacion_electronica import facturacion_electronica as fe
from facturacion_electronica.firma import Firma
import json
from lxml import etree
import unittest


def verificar_firma_xml(firma_electronica, xml):
    firma = Firma(firma_electronica)
    result = firma.verificar_firma_xml(xml)
    return result

class TestEjemploBasico33(unittest.TestCase):
    """
        Test Set Básico 33
    """
    def test_timbrar_y_enviar(self):
        """
        Test Set Básico 33
        """
        print("Se inicia test básico 33")
        f = open("facturacion_electronica/ejemplos/ejemplo_basico_33.json")
        txt_json = f.read()
        f.close()
        ejemplo_33 = json.loads(txt_json)
        firma_electronica = ejemplo_33['firma_electronica'].copy()
        result = fe.timbrar_y_enviar(ejemplo_33)
        self.assertFalse(result.get('errores', False))
        self.assertTrue(result.get('sii_xml_request', False))
        """
            verificar firma Envio
        """
        result_firma = verificar_firma_xml(
            firma_electronica.copy(),
            result['sii_xml_request'])
        self.assertEqual((0,''), result_firma)
        """
            Verifico Integridad XML
        """
        xml = etree.fromstring(
            result['sii_xml_request'].replace('xmlns="http://www.sii.cl/SiiDte"',
                                             '').encode('ISO-8859-1'))
        query = "SetDTE/Caratula/SubTotDTE"
        SubTotDTEs = xml.findall(query)
        self.assertEqual(len(SubTotDTEs), 3)
        for SubTotDTE in SubTotDTEs:
            """
                Verifico cantidades en carátula
            """
            if SubTotDTE.find("TpoDTE").text == '33':
                self.assertEqual(
                    SubTotDTE.find("NroDTE").text, "4")
            elif SubTotDTE.find("TpoDTE").text == '61':
                self.assertEqual(
                    SubTotDTE.find("NroDTE").text, "3")
            elif SubTotDTE.find("TpoDTE").text == '56':
                self.assertEqual(
                    SubTotDTE.find("NroDTE").text, "1")
        query = "SetDTE/DTE"
        DTEs = xml.findall(query)
        self.assertEqual(len(DTEs), 8)
        self.assertEqual(len(result.get('detalles', [])), 8)
        for dte in result['detalles']:
            """
                Verifico DTE individuales
            """
            self.assertTrue(dte.get('NroDTE'))
            self.assertTrue(dte.get('sii_barcode_img'))
            self.assertTrue(dte.get('sii_xml_dte'))
            string_xml_dte = '<?xml version="1.0" encoding="ISO-8859-1"?>' + \
                                dte['sii_xml_dte']
            """
                Verifico Firma DTE
            """
            result_firma = verificar_firma_xml(
                firma_electronica.copy(),
                string_xml_dte)
            self.assertEqual((0,''), result_firma)
            xml_dte = etree.fromstring(
                string_xml_dte.replace('xmlns="http://www.sii.cl/SiiDte"',
                                             '').encode('ISO-8859-1'))
            IdDoc = xml_dte.find('Documento/Encabezado/IdDoc')
            Totales = xml_dte.find('Documento/Encabezado/Totales')
            if dte['NroDTE'] == 1:
                self.assertEqual(dte['TipoDTE'], 33)
                self.assertEqual(IdDoc.find('TipoDTE').text, '33')
                self.assertEqual(dte['Folio'], 41)
                self.assertEqual(IdDoc.find('Folio').text, '41')
                self.assertEqual(dte['MntExe'], 0)
                self.assertIsNone(Totales.find('MntExe'))
                self.assertEqual(dte['MntNeto'], 1085752)
                self.assertEqual(Totales.find('MntNeto').text, '1085752')
                self.assertEqual(dte['MntIVA'], 206293)
                self.assertEqual(Totales.find('IVA').text, '206293')
                self.assertEqual(dte['MntTotal'], 1292045)
                self.assertEqual(Totales.find('MntTotal').text, '1292045')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))
            elif dte['NroDTE'] == 2:
                self.assertEqual(dte['TipoDTE'], 33)
                self.assertEqual(IdDoc.find('TipoDTE').text, '33')
                self.assertEqual(dte['Folio'], 42)
                self.assertEqual(IdDoc.find('Folio').text, '42')
                self.assertEqual(dte['MntExe'], 0)
                self.assertIsNone(Totales.find('MntExe'))
                self.assertEqual(dte['MntNeto'], 7519476)
                self.assertEqual(Totales.find('MntNeto').text, '7519476')
                self.assertEqual(dte['MntIVA'], 1428700)
                self.assertEqual(Totales.find('IVA').text, '1428700')
                self.assertEqual(dte['MntTotal'], 8948176)
                self.assertEqual(Totales.find('MntTotal').text, '8948176')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))
            elif dte['NroDTE'] == 3:
                self.assertEqual(dte['TipoDTE'], 33)
                self.assertEqual(IdDoc.find('TipoDTE').text, '33')
                self.assertEqual(dte['Folio'], 43)
                self.assertEqual(IdDoc.find('Folio').text, '43')
                self.assertEqual(dte['MntExe'], 35344)
                self.assertEqual(Totales.find('MntExe').text, '35344')
                self.assertEqual(dte['MntNeto'], 1510824)
                self.assertEqual(Totales.find('MntNeto').text, '1510824')
                self.assertEqual(dte['MntIVA'], 287057)
                self.assertEqual(Totales.find('IVA').text, '287057')
                self.assertEqual(dte['MntTotal'], 1833225)
                self.assertEqual(Totales.find('MntTotal').text, '1833225')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))
            elif dte['NroDTE'] == 4:
                self.assertEqual(dte['TipoDTE'], 33)
                self.assertEqual(IdDoc.find('TipoDTE').text, '33')
                self.assertEqual(dte['Folio'], 44)
                self.assertEqual(IdDoc.find('Folio').text, '44')
                self.assertEqual(dte['MntExe'], 13678)
                self.assertEqual(Totales.find('MntExe').text, '13678')
                self.assertEqual(dte['MntNeto'], 3226933)
                self.assertEqual(Totales.find('MntNeto').text, '3226933')
                self.assertEqual(dte['MntIVA'], 613117)
                self.assertEqual(Totales.find('IVA').text, '613117')
                self.assertEqual(dte['MntTotal'], 3853728)
                self.assertEqual(Totales.find('MntTotal').text, '3853728')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))
            elif dte['NroDTE'] == 5:
                self.assertEqual(dte['TipoDTE'], 61)
                self.assertEqual(IdDoc.find('TipoDTE').text, '61')
                self.assertEqual(dte['Folio'], 21)
                self.assertEqual(IdDoc.find('Folio').text, '21')
                self.assertEqual(dte['MntExe'], 0)
                self.assertIsNone(Totales.find('MntExe'))
                self.assertEqual(dte['MntNeto'], 1085752)
                self.assertEqual(Totales.find('MntNeto').text, '1085752')
                self.assertEqual(dte['MntIVA'], 206293)
                self.assertEqual(Totales.find('IVA').text, '206293')
                self.assertEqual(dte['MntTotal'], 1292045)
                self.assertEqual(Totales.find('MntTotal').text, '1292045')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))
            elif dte['NroDTE'] == 6:
                self.assertEqual(dte['TipoDTE'], 61)
                self.assertEqual(IdDoc.find('TipoDTE').text, '61')
                self.assertEqual(dte['Folio'], 22)
                self.assertEqual(IdDoc.find('Folio').text, '22')
                self.assertEqual(dte['MntExe'], 0)
                self.assertIsNone(Totales.find('MntExe'))
                self.assertEqual(dte['MntNeto'], 3698268)
                self.assertEqual(Totales.find('MntNeto').text, '3698268')
                self.assertEqual(dte['MntIVA'], 702671)
                self.assertEqual(Totales.find('IVA').text, '702671')
                self.assertEqual(dte['MntTotal'], 4400939)
                self.assertEqual(Totales.find('MntTotal').text, '4400939')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))
            elif dte['NroDTE'] == 7:
                self.assertEqual(dte['TipoDTE'], 61)
                self.assertEqual(IdDoc.find('TipoDTE').text, '61')
                self.assertEqual(dte['Folio'], 23)
                self.assertEqual(IdDoc.find('Folio').text, '23')
                self.assertEqual(dte['MntExe'], 35344)
                self.assertEqual(Totales.find('MntExe').text, '35344')
                self.assertEqual(dte['MntNeto'], 1510824)
                self.assertEqual(Totales.find('MntNeto').text, '1510824')
                self.assertEqual(dte['MntIVA'], 287057)
                self.assertEqual(Totales.find('IVA').text, '287057')
                self.assertEqual(dte['MntTotal'], 1833225)
                self.assertEqual(Totales.find('MntTotal').text, '1833225')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))
            elif dte['NroDTE'] == 8:
                self.assertEqual(dte['TipoDTE'], 56)
                self.assertEqual(IdDoc.find('TipoDTE').text, '56')
                self.assertEqual(dte['Folio'], 7)
                self.assertEqual(IdDoc.find('Folio').text, '7')
                self.assertEqual(dte['MntExe'], 0)
                self.assertIsNone(Totales.find('MntExe'))
                self.assertEqual(dte['MntNeto'], 1085752)
                self.assertEqual(Totales.find('MntNeto').text, '1085752')
                self.assertEqual(dte['MntIVA'], 206293)
                self.assertEqual(Totales.find('IVA').text, '206293')
                self.assertEqual(dte['MntTotal'], 1292045)
                self.assertEqual(Totales.find('MntTotal').text, '1292045')
                self.assertEqual(dte['ImptoReten'], 0)
                self.assertIsNone(Totales.find('ImptoReten'))

if __name__ == '__main__':
    unittest.main()
