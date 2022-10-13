from rdkit import Chem

def mol_adjust_hpolar(mol):
    mol = Chem.RemoveHs(mol)
    polar_atoms = [atom.GetIdx() for atom in mol.GetAtoms() if atom.GetSymbol() != 'C']
    if len(polar_atoms):
        mol = Chem.AddHs(mol, onlyOnAtoms=polar_atoms)
        
    return mol

def is_iso_mol(iso_mol, mol):
    if iso_mol.GetSubstructMatch(mol, useChirality=True):
        return True
    else:
        return False

def is_iso_smiles(iso_smi, smi):
    mol = Chem.MolFromSmiles(smi)
    iso_mol = Chem.MolFromSmiles(iso_smi)
    
    if is_iso_mol(iso_mol, mol):
        return True
    else:
        return False

def get_actual_smiles(mol):
    mol_copy = Chem.Mol(mol)
    Chem.rdmolops.AssignStereochemistryFrom3D(mol_copy)
    mol_copy = Chem.RemoveHs(mol_copy)
    
    return Chem.MolToSmiles(mol_copy, canonical=True, isomericSmiles=True, kekuleSmiles=True)
