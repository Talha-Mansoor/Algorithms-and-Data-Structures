//Talha Mansoor
//kgy284
//11346490
//CMPT 280
//Noah Ortega

import lib280.list.LinkedList280;
import lib280.tree.BasicMAryTree280;

public class SkillTree extends BasicMAryTree280<Skill> {

	/**	
	 * Create lib280.tree with the specified root node and
	 * specified maximum arity of nodes.  
	 * @timing O(1) 
	 * @param x item to set as the root node
	 * @param m number of children allowed for future nodes 
	 */
	public SkillTree(Skill x, int m)
	{
		super(x,m);
	}

	/**
	 * A convenience method that avoids typecasts.
	 * Obtains a subtree of the root.
	 * 
	 * @param i Index of the desired subtree of the root.
	 * @return the i-th subtree of the root.
	 */
	public SkillTree rootSubTree(int i) {
		return (SkillTree)super.rootSubtree(i);
	}


	public void printContents() {
		if(!this.isEmpty())
			printContents(this.rootNode);
	}
	protected void printContents(Skill x) {
		System.out.println(this.rootItem().toString());
		for(int i = 1; i <= this.rootArity(); i++) {
			if(this.subnode(i) != null) {
				printContents(root.subnode(i));
			}
		}

	public static void main(String[] args) {

		Skill HP=new Skill("HP","Increases total health",1);
		SkillTree tHP=new SkillTree(HP,2);

		Skill Strength=new Skill("Strength","Increases physical attack power",1);
		SkillTree tStrength=new SkillTree(Strength,2);
		Skill Magic=new Skill("Magic","Increases Magic attack",1);
		SkillTree tMagic=new SkillTree(Magic,2);


		Skill Dexterity=new Skill("Dexterity","Increases attack speec",1);
		SkillTree tDexterity=new SkillTree(Dexterity,2);
		Skill Speed=new Skill("Speed","Increases movement speed",1);
		SkillTree tSpeed=new SkillTree(Speed,2);

		Skill MResistance=new Skill("Magic Resistance","Increases magic resistance",1);
		SkillTree tMResistance=new SkillTree(MResistance,2);
		Skill Mana=new Skill("Mana","Increases total mana",1);
		SkillTree tMana=new SkillTree(Mana,2);

		Skill PResistance=new Skill("Poison Resistance", "Reduces effect of poison",1);
		SkillTree tPResistance=new SkillTree(PResistance,2);
		Skill Endurance=new Skill("Endurance","increases stamina so player can sprint longer",1);
		SkillTree tEndurance=new SkillTree(Endurance,2);

		Skill Luck=new Skill("Luck","Avoid enemy Hit detection",1);
		SkillTree tLuck=new SkillTree(Luck,2);

		tHP.setRootSubtree(tStrength,1);
		tHP.setRootSubtree(tMagic,2);
		tStrength.setRootSubtree(tDexterity,1);
		tStrength.setRootSubtree(tSpeed,2);

		tMagic.setRootSubtree(tMResistance,1);
		tMagic.setRootSubtree(tMana,2);

		tDexterity.setRootSubtree(tPResistance,1);
		tDexterity.setRootSubtree(tEndurance,2);

		tSpeed.setRootSubtree(tLuck,1);

		System.out.println(tHP.toStringByLevel());



	}
	

}
